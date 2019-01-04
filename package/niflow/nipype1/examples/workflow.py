# This file demonstrates a workflow-generating function, a particular convention for generating
# nipype workflows. Others are possible.

# Every workflow need pe.Workflow [0] and pe.Node [1], and most will need basic utility
# interfaces [2].
# [0] https://nipype.rtfd.io/en/latest/api/generated/nipype.pipeline.engine.workflows.html
# [1] https://nipype.rtfd.io/en/latest/api/generated/nipype.pipeline.engine.nodes.html
# [2] https://nipype.rtfd.io/en/latest/interfaces/generated/nipype.interfaces.utility/base.html
from nipype.pipeline import engine as pe
from nipype.interfaces import utility as niu

def init_examples_wf(name='examples_wf'):
    wf = pe.Workflow(name=name)

    # inputnode/outputnode can be thought of as the parameters and return values of a function
    inputnode = pe.Node(niu.IdentityInterface(['in_file']), name='inputnode')
    outputnode = pe.Node(niu.IdentityInterface(['out_file']), name='outputnode')

    #
    # The rest of the workflow should be defined here.
    #

    wf.connect([
        ## Connect fields from one interface to another, e.g.,
        # (inputnode, some_node_1, [('in_file', 'in_file')]),
        # ...
        # (some_node_n, outputnode, [('out_file', 'out_file')]),
        ])

    return wf
