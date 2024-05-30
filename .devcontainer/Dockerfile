FROM mcr.microsoft.com/devcontainers/anaconda:0-3

## Install packages via Conda - fails for Github code spaces
#COPY conda-environment/environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
#RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
#    && rm -rf /tmp/conda-tmp

## Install packages via Pip
COPY requirements.txt /tmp/pip-tmp/
RUN /opt/conda/bin/python -m pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt ; \
    rm -rf /tmp/pip-tmp/requirements.txt

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
