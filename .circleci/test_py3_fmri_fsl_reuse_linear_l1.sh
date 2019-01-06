#!/bin/bash

docker run --rm=false -t -v $WORKDIR:/work -v $HOME/examples:/data/examples:ro -w /work "${DOCKER_IMAGE}:py36" niflow-nipype1-examples fmri_fsl_reuse Linear /data/examples/ level1_workflow
