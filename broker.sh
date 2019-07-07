#!/bin/bash
celery -A django_test worker -l info >> /tmp/celery.log