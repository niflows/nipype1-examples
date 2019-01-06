#!/bin/bash

docker run --rm=false -t -v $WORKDIR:/work -v $HOME/examples:/data/examples:ro -w /work "${DOCKER_IMAGE}:py36" niflow-nipype1-examples fmri_fsl_feeds Linear /data/examples/ l1pipeline
