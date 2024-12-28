#!/bin/bash

repo_dir=$(git rev-parse --show-toplevel)
proj_root=$(dirname "$(readlink -f $0)")

docker build -t synthbot/node_graph_server -f "$proj_root"/Dockerfile "$repo_dir"
