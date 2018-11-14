#!/bin/bash
coverage3 run -m camera_app.tests.testStatic
coverage3 run -am camera_app.tests.testMotion
