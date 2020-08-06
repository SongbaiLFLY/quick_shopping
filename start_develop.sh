#!/bin/bash

docker-compose -f docker/docker-compose.yml up -d
docker-compose -f docker/docker-compose.yml exec quick_shopping_sanic bash
