#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
===========================
Inspecting workflow results
===========================

It can be useful to investigate individual nodes' inputs and outputs in a workflow that has been run.
For example, this can help developers write unit tests for their workflows.

"""
import os

from nipype.interfaces import utility as niu
from nipype.interfaces.base import (BaseInterfaceInputSpec, File,
                                    SimpleInterface, TraitedSpec, traits)
from nipype.pipeline import engine as pe

# First, let's start by creating a simple interface to use in our workflow.
# The WriteString interface just writes a string to a file.


class _WriteStringInputSpec(BaseInterfaceInputSpec):
    in_str = traits.Str(mandatory=True)


class _WriteStringOutputSpec(TraitedSpec):
    out_file = File(exists=True)


class WriteString(SimpleInterface):
    """Write a string to a file."""

    input_spec = _WriteStringInputSpec
    output_spec = _WriteStringOutputSpec

    def _run_interface(self, runtime):
        self._results["out_file"] = os.path.join(runtime.cwd, "out_file.txt")
        with open(self._results["out_file"], "w") as fo:
            fo.write(self.inputs.in_str)

        return runtime


# Now, we can create our workflow.
# The workflow is very simple- an inputnode, a middle node, and an outputnode.
wf = pe.Workflow(name="example_workflow")

inputnode = pe.Node(
    niu.IdentityInterface(fields=["in_str"]),
    name="inputnode",
)
outputnode = pe.Node(
    niu.IdentityInterface(fields=["out_file"]),
    name="outputnode",
)
write_string = pe.Node(
    WriteString(),
    name="write_string",
)

# fmt:off
wf.connect([
    (inputnode, write_string, [("in_str", "in_str")]),
    (write_string, outputnode, [("out_file", "out_file")]),
])
# fmt:on

# At this point, we have our basic workflow structure, so we can set inputs and run it.
wf.inputs.inputnode.in_str = "hello world"
wf.base_dir = "."
results = wf.run()

# Here we define a simple function to make it easier to grab the nodes from the results object.


def get_nodes(wf_results):
    """Load nodes from a Nipype workflow's results."""
    return {node.fullname: node for node in wf_results.nodes}


# Let's grab the nodes and check their contents!
nodes = get_nodes(results)
out_file = nodes["example_workflow.write_string"].get_output("out_file")
with open(out_file, "r") as fo:
    print(fo.read())  # "hello world"

# The same approach can be used to inspect inputs and outputs of individual nodes within a
# workflow (except for identity interfaces),
# so developers can write tests that check every element of a workflow,
# rather than just the final product.
