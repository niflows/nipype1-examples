#!/bin/bash

docker run --rm=false -t -v $WORKDIR:/work -v $HOME/examples:/data/examples:ro -w /work "${DOCKER_IMAGE}:py36" niflow-nipype1-examples test_spm Linear /data/examples/ workflow3d
