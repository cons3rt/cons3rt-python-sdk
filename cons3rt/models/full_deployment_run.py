"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration

__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'


class FullDeploymentRun(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'categories': 'list[MinimalCategory]',
        'creator': 'MinimalUser',
        'earliest_start_time': 'datetime',
        'end_time': 'datetime',
        'lease_time': 'datetime',
        'estimated_ready_time': 'datetime',
        'estimated_start_time': 'datetime',
        'id': 'int',
        'log_entries': 'list[MinimalLogEntry]',
        'message': 'str',
        'project': 'MinimalProject',
        'ready_time': 'datetime',
        'result': 'str',
        'start_time': 'datetime',
        'time_of_request': 'datetime',
        'canceled': 'bool',
        'deployment': 'MinimalDeployment',
        'deployment_run_hosts': 'list[MinimalDeploymentRunHost]',
        'properties': 'list[ModelProperty]',
        'deployment_run_status': 'str',
        'description': 'str',
        'fap_status': 'str',
        'host_set_name': 'str',
        'locked': 'bool',
        'name': 'str',
        'power_schedule': 'PowerSchedule',
        'recurring_schedule': 'MinimalRecurringSchedule',
        'scheduler_status_message': 'str',
        'target_state': 'str',
        'test_error': 'bool',
        'test_runs': 'list[MinimalTestRunTask]',
        'retained_on_error': 'bool',
        'virtualization_realm': 'MinimalVirtualizationRealm',
        'deployment_run_result_type': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'creator': 'creator',
        'earliest_start_time': 'earliestStartTime',
        'end_time': 'endTime',
        'lease_time': 'leaseTime',
        'estimated_ready_time': 'estimatedReadyTime',
        'estimated_start_time': 'estimatedStartTime',
        'id': 'id',
        'log_entries': 'logEntries',
        'message': 'message',
        'project': 'project',
        'ready_time': 'readyTime',
        'result': 'result',
        'start_time': 'startTime',
        'time_of_request': 'timeOfRequest',
        'canceled': 'canceled',
        'deployment': 'deployment',
        'deployment_run_hosts': 'deploymentRunHosts',
        'properties': 'properties',
        'deployment_run_status': 'deploymentRunStatus',
        'description': 'description',
        'fap_status': 'fapStatus',
        'host_set_name': 'hostSetName',
        'locked': 'locked',
        'name': 'name',
        'power_schedule': 'powerSchedule',
        'recurring_schedule': 'recurringSchedule',
        'scheduler_status_message': 'schedulerStatusMessage',
        'target_state': 'targetState',
        'test_error': 'testError',
        'test_runs': 'testRuns',
        'retained_on_error': 'retainedOnError',
        'virtualization_realm': 'virtualizationRealm',
        'deployment_run_result_type': 'deploymentRunResultType'
    }

    def __init__(self, categories=None, creator=None, earliest_start_time=None, end_time=None, lease_time=None, estimated_ready_time=None, estimated_start_time=None, id=None, log_entries=None, message=None, project=None, ready_time=None, result=None, start_time=None, time_of_request=None, canceled=None, deployment=None, deployment_run_hosts=None, properties=None, deployment_run_status=None, description=None, fap_status=None, host_set_name=None, locked=None, name=None, power_schedule=None, recurring_schedule=None, scheduler_status_message=None, target_state=None, test_error=None, test_runs=None, retained_on_error=None, virtualization_realm=None, deployment_run_result_type=None, local_vars_configuration=None):  # noqa: E501
        """FullDeploymentRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._categories = None
        self._creator = None
        self._earliest_start_time = None
        self._end_time = None
        self._lease_time = None
        self._estimated_ready_time = None
        self._estimated_start_time = None
        self._id = None
        self._log_entries = None
        self._message = None
        self._project = None
        self._ready_time = None
        self._result = None
        self._start_time = None
        self._time_of_request = None
        self._canceled = None
        self._deployment = None
        self._deployment_run_hosts = None
        self._properties = None
        self._deployment_run_status = None
        self._description = None
        self._fap_status = None
        self._host_set_name = None
        self._locked = None
        self._name = None
        self._power_schedule = None
        self._recurring_schedule = None
        self._scheduler_status_message = None
        self._target_state = None
        self._test_error = None
        self._test_runs = None
        self._retained_on_error = None
        self._virtualization_realm = None
        self._deployment_run_result_type = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if creator is not None:
            self.creator = creator
        if earliest_start_time is not None:
            self.earliest_start_time = earliest_start_time
        if end_time is not None:
            self.end_time = end_time
        if lease_time is not None:
            self.lease_time = lease_time
        if estimated_ready_time is not None:
            self.estimated_ready_time = estimated_ready_time
        if estimated_start_time is not None:
            self.estimated_start_time = estimated_start_time
        if id is not None:
            self.id = id
        if log_entries is not None:
            self.log_entries = log_entries
        if message is not None:
            self.message = message
        if project is not None:
            self.project = project
        if ready_time is not None:
            self.ready_time = ready_time
        if result is not None:
            self.result = result
        if start_time is not None:
            self.start_time = start_time
        if time_of_request is not None:
            self.time_of_request = time_of_request
        if canceled is not None:
            self.canceled = canceled
        if deployment is not None:
            self.deployment = deployment
        if deployment_run_hosts is not None:
            self.deployment_run_hosts = deployment_run_hosts
        if properties is not None:
            self.properties = properties
        if deployment_run_status is not None:
            self.deployment_run_status = deployment_run_status
        if description is not None:
            self.description = description
        if fap_status is not None:
            self.fap_status = fap_status
        if host_set_name is not None:
            self.host_set_name = host_set_name
        if locked is not None:
            self.locked = locked
        if name is not None:
            self.name = name
        if power_schedule is not None:
            self.power_schedule = power_schedule
        if recurring_schedule is not None:
            self.recurring_schedule = recurring_schedule
        if scheduler_status_message is not None:
            self.scheduler_status_message = scheduler_status_message
        if target_state is not None:
            self.target_state = target_state
        if test_error is not None:
            self.test_error = test_error
        if test_runs is not None:
            self.test_runs = test_runs
        if retained_on_error is not None:
            self.retained_on_error = retained_on_error
        if virtualization_realm is not None:
            self.virtualization_realm = virtualization_realm
        if deployment_run_result_type is not None:
            self.deployment_run_result_type = deployment_run_result_type

    @property
    def categories(self):
        """Gets the categories of this FullDeploymentRun.  # noqa: E501


        :return: The categories of this FullDeploymentRun.  # noqa: E501
        :rtype: list[MinimalCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this FullDeploymentRun.


        :param categories: The categories of this FullDeploymentRun.  # noqa: E501
        :type: list[MinimalCategory]
        """

        self._categories = categories

    @property
    def creator(self):
        """Gets the creator of this FullDeploymentRun.  # noqa: E501


        :return: The creator of this FullDeploymentRun.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FullDeploymentRun.


        :param creator: The creator of this FullDeploymentRun.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

    @property
    def earliest_start_time(self):
        """Gets the earliest_start_time of this FullDeploymentRun.  # noqa: E501


        :return: The earliest_start_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_start_time

    @earliest_start_time.setter
    def earliest_start_time(self, earliest_start_time):
        """Sets the earliest_start_time of this FullDeploymentRun.


        :param earliest_start_time: The earliest_start_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._earliest_start_time = earliest_start_time

    @property
    def end_time(self):
        """Gets the end_time of this FullDeploymentRun.  # noqa: E501


        :return: The end_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FullDeploymentRun.


        :param end_time: The end_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def lease_time(self):
        """Gets the lease_time of this FullDeploymentRun.  # noqa: E501


        :return: The lease_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._lease_time

    @lease_time.setter
    def lease_time(self, lease_time):
        """Sets the lease_time of this FullDeploymentRun.


        :param lease_time: The lease_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._lease_time = lease_time

    @property
    def estimated_ready_time(self):
        """Gets the estimated_ready_time of this FullDeploymentRun.  # noqa: E501


        :return: The estimated_ready_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._estimated_ready_time

    @estimated_ready_time.setter
    def estimated_ready_time(self, estimated_ready_time):
        """Sets the estimated_ready_time of this FullDeploymentRun.


        :param estimated_ready_time: The estimated_ready_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._estimated_ready_time = estimated_ready_time

    @property
    def estimated_start_time(self):
        """Gets the estimated_start_time of this FullDeploymentRun.  # noqa: E501


        :return: The estimated_start_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._estimated_start_time

    @estimated_start_time.setter
    def estimated_start_time(self, estimated_start_time):
        """Sets the estimated_start_time of this FullDeploymentRun.


        :param estimated_start_time: The estimated_start_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._estimated_start_time = estimated_start_time

    @property
    def id(self):
        """Gets the id of this FullDeploymentRun.  # noqa: E501


        :return: The id of this FullDeploymentRun.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FullDeploymentRun.


        :param id: The id of this FullDeploymentRun.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def log_entries(self):
        """Gets the log_entries of this FullDeploymentRun.  # noqa: E501


        :return: The log_entries of this FullDeploymentRun.  # noqa: E501
        :rtype: list[MinimalLogEntry]
        """
        return self._log_entries

    @log_entries.setter
    def log_entries(self, log_entries):
        """Sets the log_entries of this FullDeploymentRun.


        :param log_entries: The log_entries of this FullDeploymentRun.  # noqa: E501
        :type: list[MinimalLogEntry]
        """

        self._log_entries = log_entries

    @property
    def message(self):
        """Gets the message of this FullDeploymentRun.  # noqa: E501


        :return: The message of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FullDeploymentRun.


        :param message: The message of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def project(self):
        """Gets the project of this FullDeploymentRun.  # noqa: E501


        :return: The project of this FullDeploymentRun.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this FullDeploymentRun.


        :param project: The project of this FullDeploymentRun.  # noqa: E501
        :type: MinimalProject
        """

        self._project = project

    @property
    def ready_time(self):
        """Gets the ready_time of this FullDeploymentRun.  # noqa: E501


        :return: The ready_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._ready_time

    @ready_time.setter
    def ready_time(self, ready_time):
        """Sets the ready_time of this FullDeploymentRun.


        :param ready_time: The ready_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._ready_time = ready_time

    @property
    def result(self):
        """Gets the result of this FullDeploymentRun.  # noqa: E501


        :return: The result of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FullDeploymentRun.


        :param result: The result of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this FullDeploymentRun.  # noqa: E501


        :return: The start_time of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this FullDeploymentRun.


        :param start_time: The start_time of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def time_of_request(self):
        """Gets the time_of_request of this FullDeploymentRun.  # noqa: E501


        :return: The time_of_request of this FullDeploymentRun.  # noqa: E501
        :rtype: datetime
        """
        return self._time_of_request

    @time_of_request.setter
    def time_of_request(self, time_of_request):
        """Sets the time_of_request of this FullDeploymentRun.


        :param time_of_request: The time_of_request of this FullDeploymentRun.  # noqa: E501
        :type: datetime
        """

        self._time_of_request = time_of_request

    @property
    def canceled(self):
        """Gets the canceled of this FullDeploymentRun.  # noqa: E501


        :return: The canceled of this FullDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this FullDeploymentRun.


        :param canceled: The canceled of this FullDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._canceled = canceled

    @property
    def deployment(self):
        """Gets the deployment of this FullDeploymentRun.  # noqa: E501


        :return: The deployment of this FullDeploymentRun.  # noqa: E501
        :rtype: MinimalDeployment
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this FullDeploymentRun.


        :param deployment: The deployment of this FullDeploymentRun.  # noqa: E501
        :type: MinimalDeployment
        """

        self._deployment = deployment

    @property
    def deployment_run_hosts(self):
        """Gets the deployment_run_hosts of this FullDeploymentRun.  # noqa: E501


        :return: The deployment_run_hosts of this FullDeploymentRun.  # noqa: E501
        :rtype: list[MinimalDeploymentRunHost]
        """
        return self._deployment_run_hosts

    @deployment_run_hosts.setter
    def deployment_run_hosts(self, deployment_run_hosts):
        """Sets the deployment_run_hosts of this FullDeploymentRun.


        :param deployment_run_hosts: The deployment_run_hosts of this FullDeploymentRun.  # noqa: E501
        :type: list[MinimalDeploymentRunHost]
        """

        self._deployment_run_hosts = deployment_run_hosts

    @property
    def properties(self):
        """Gets the properties of this FullDeploymentRun.  # noqa: E501


        :return: The properties of this FullDeploymentRun.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this FullDeploymentRun.


        :param properties: The properties of this FullDeploymentRun.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def deployment_run_status(self):
        """Gets the deployment_run_status of this FullDeploymentRun.  # noqa: E501


        :return: The deployment_run_status of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_status

    @deployment_run_status.setter
    def deployment_run_status(self, deployment_run_status):
        """Sets the deployment_run_status of this FullDeploymentRun.


        :param deployment_run_status: The deployment_run_status of this FullDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SCHEDULED", "SUBMITTED", "PROVISIONING_HOSTS", "HOSTS_PROVISIONED", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "TESTING", "TESTED", "COMPLETED", "CANCELED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_run_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_run_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_run_status, allowed_values)
            )

        self._deployment_run_status = deployment_run_status

    @property
    def description(self):
        """Gets the description of this FullDeploymentRun.  # noqa: E501


        :return: The description of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FullDeploymentRun.


        :param description: The description of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fap_status(self):
        """Gets the fap_status of this FullDeploymentRun.  # noqa: E501


        :return: The fap_status of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._fap_status

    @fap_status.setter
    def fap_status(self, fap_status):
        """Sets the fap_status of this FullDeploymentRun.


        :param fap_status: The fap_status of this FullDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "BUILDING_HOSTSET", "BUILDING_HOSTSET_ERROR", "HOSTSET_BUILT_POWERED_OFF", "POWERING_ON", "POWERING_ON_ERROR", "POWERED_ON", "AWAITING_AGENT_CHECK_IN", "AGENT_CHECK_IN_ERROR", "AGENT_CHECK_IN_SUCCESS", "BUILDING_SOURCE", "SOURCE_BUILT", "BUILDING_SOURCE_ERROR", "BUILDING_SYSTEMS", "BUILDING_SYSTEMS_ERROR", "SYSTEMS_BUILT", "BUILDING_SCENARIO", "BUILDING_SCENARIO_ERROR", "SCENARIO_BUILT", "REBOOTING", "REBOOTING_ERROR", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "RELEASING_SCENARIO_ERROR", "COMPLETE", "UNKNOWN", "CANCELED", "INVALID_STATE_ERROR", "FAP_SERVICE_COMMUNICATIONS_ERROR", "INVALID_REQUEST_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fap_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fap_status` ({0}), must be one of {1}"  # noqa: E501
                .format(fap_status, allowed_values)
            )

        self._fap_status = fap_status

    @property
    def host_set_name(self):
        """Gets the host_set_name of this FullDeploymentRun.  # noqa: E501


        :return: The host_set_name of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._host_set_name

    @host_set_name.setter
    def host_set_name(self, host_set_name):
        """Sets the host_set_name of this FullDeploymentRun.


        :param host_set_name: The host_set_name of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._host_set_name = host_set_name

    @property
    def locked(self):
        """Gets the locked of this FullDeploymentRun.  # noqa: E501


        :return: The locked of this FullDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this FullDeploymentRun.


        :param locked: The locked of this FullDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """Gets the name of this FullDeploymentRun.  # noqa: E501


        :return: The name of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FullDeploymentRun.


        :param name: The name of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def power_schedule(self):
        """Gets the power_schedule of this FullDeploymentRun.  # noqa: E501


        :return: The power_schedule of this FullDeploymentRun.  # noqa: E501
        :rtype: PowerSchedule
        """
        return self._power_schedule

    @power_schedule.setter
    def power_schedule(self, power_schedule):
        """Sets the power_schedule of this FullDeploymentRun.


        :param power_schedule: The power_schedule of this FullDeploymentRun.  # noqa: E501
        :type: PowerSchedule
        """

        self._power_schedule = power_schedule

    @property
    def recurring_schedule(self):
        """Gets the recurring_schedule of this FullDeploymentRun.  # noqa: E501


        :return: The recurring_schedule of this FullDeploymentRun.  # noqa: E501
        :rtype: MinimalRecurringSchedule
        """
        return self._recurring_schedule

    @recurring_schedule.setter
    def recurring_schedule(self, recurring_schedule):
        """Sets the recurring_schedule of this FullDeploymentRun.


        :param recurring_schedule: The recurring_schedule of this FullDeploymentRun.  # noqa: E501
        :type: MinimalRecurringSchedule
        """

        self._recurring_schedule = recurring_schedule

    @property
    def scheduler_status_message(self):
        """Gets the scheduler_status_message of this FullDeploymentRun.  # noqa: E501


        :return: The scheduler_status_message of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_status_message

    @scheduler_status_message.setter
    def scheduler_status_message(self, scheduler_status_message):
        """Sets the scheduler_status_message of this FullDeploymentRun.


        :param scheduler_status_message: The scheduler_status_message of this FullDeploymentRun.  # noqa: E501
        :type: str
        """

        self._scheduler_status_message = scheduler_status_message

    @property
    def target_state(self):
        """Gets the target_state of this FullDeploymentRun.  # noqa: E501


        :return: The target_state of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this FullDeploymentRun.


        :param target_state: The target_state of this FullDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_STATE", "SYSTEMS_BUILT", "SCENARIO_BUILT", "TESTS_EXECUTED_RESOURCES_RELEASED", "TESTS_EXECUTED_RESOURCES_RESERVED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and target_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `target_state` ({0}), must be one of {1}"  # noqa: E501
                .format(target_state, allowed_values)
            )

        self._target_state = target_state

    @property
    def test_error(self):
        """Gets the test_error of this FullDeploymentRun.  # noqa: E501


        :return: The test_error of this FullDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._test_error

    @test_error.setter
    def test_error(self, test_error):
        """Sets the test_error of this FullDeploymentRun.


        :param test_error: The test_error of this FullDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._test_error = test_error

    @property
    def test_runs(self):
        """Gets the test_runs of this FullDeploymentRun.  # noqa: E501


        :return: The test_runs of this FullDeploymentRun.  # noqa: E501
        :rtype: list[MinimalTestRunTask]
        """
        return self._test_runs

    @test_runs.setter
    def test_runs(self, test_runs):
        """Sets the test_runs of this FullDeploymentRun.


        :param test_runs: The test_runs of this FullDeploymentRun.  # noqa: E501
        :type: list[MinimalTestRunTask]
        """

        self._test_runs = test_runs

    @property
    def retained_on_error(self):
        """Gets the retained_on_error of this FullDeploymentRun.  # noqa: E501


        :return: The retained_on_error of this FullDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._retained_on_error

    @retained_on_error.setter
    def retained_on_error(self, retained_on_error):
        """Sets the retained_on_error of this FullDeploymentRun.


        :param retained_on_error: The retained_on_error of this FullDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._retained_on_error = retained_on_error

    @property
    def virtualization_realm(self):
        """Gets the virtualization_realm of this FullDeploymentRun.  # noqa: E501


        :return: The virtualization_realm of this FullDeploymentRun.  # noqa: E501
        :rtype: MinimalVirtualizationRealm
        """
        return self._virtualization_realm

    @virtualization_realm.setter
    def virtualization_realm(self, virtualization_realm):
        """Sets the virtualization_realm of this FullDeploymentRun.


        :param virtualization_realm: The virtualization_realm of this FullDeploymentRun.  # noqa: E501
        :type: MinimalVirtualizationRealm
        """

        self._virtualization_realm = virtualization_realm

    @property
    def deployment_run_result_type(self):
        """Gets the deployment_run_result_type of this FullDeploymentRun.  # noqa: E501


        :return: The deployment_run_result_type of this FullDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_result_type

    @deployment_run_result_type.setter
    def deployment_run_result_type(self, deployment_run_result_type):
        """Sets the deployment_run_result_type of this FullDeploymentRun.


        :param deployment_run_result_type: The deployment_run_result_type of this FullDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "SUCCESS", "CANCELED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_run_result_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_run_result_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_run_result_type, allowed_values)
            )

        self._deployment_run_result_type = deployment_run_result_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullDeploymentRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullDeploymentRun):
            return True

        return self.to_dict() != other.to_dict()
