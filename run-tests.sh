#!/bin/sh

#  Copyright 2016 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

set -ev

pip freeze | grep -qi pyrivet || {
    echo "You must install pyrivet in editable mode using \"pip install -e\"
     before calling "$(basename "$0")
    exit 1
}

mpi_command=mpiexec
if [ ! -z $SLURM_NODELIST ]
then
    mpi_command=srun
fi
$mpi_command -n 2 coverage run -m pytest

coverage combine

# Travis error workaround
coverage_report=$(mktemp -u coverage_report_XXXXX) || {
    echo "mktemp -u error" >&2;
    exit 1;
}

set +e
coverage report > $coverage_report
report_exit_code=$?

coverage html
coverage xml

cat $coverage_report
rm $coverage_report

if [ $report_exit_code = 2 ]
then
    echo "ERROR: Coverage too low."
fi
exit $report_exit_code
