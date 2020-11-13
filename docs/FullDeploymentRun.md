# FullDeploymentRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**list[MinimalCategory]**](MinimalCategory.md) |  | [optional] 
**creator** | [**MinimalUser**](MinimalUser.md) |  | [optional] 
**earliest_start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**lease_time** | **datetime** |  | [optional] 
**estimated_ready_time** | **datetime** |  | [optional] 
**estimated_start_time** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**log_entries** | [**list[MinimalLogEntry]**](MinimalLogEntry.md) |  | [optional] 
**message** | **str** |  | [optional] 
**project** | [**MinimalProject**](MinimalProject.md) |  | [optional] 
**ready_time** | **datetime** |  | [optional] 
**result** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**time_of_request** | **datetime** |  | [optional] 
**canceled** | **bool** |  | [optional] 
**deployment** | [**MinimalDeployment**](MinimalDeployment.md) |  | [optional] 
**deployment_run_hosts** | [**list[MinimalDeploymentRunHost]**](MinimalDeploymentRunHost.md) |  | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) |  | [optional] 
**deployment_run_status** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fap_status** | **str** |  | [optional] 
**host_set_name** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**power_schedule** | [**PowerSchedule**](PowerSchedule.md) |  | [optional] 
**recurring_schedule** | [**MinimalRecurringSchedule**](MinimalRecurringSchedule.md) |  | [optional] 
**scheduler_status_message** | **str** |  | [optional] 
**target_state** | **str** |  | [optional] 
**test_error** | **bool** |  | [optional] 
**test_runs** | [**list[MinimalTestRunTask]**](MinimalTestRunTask.md) |  | [optional] 
**retained_on_error** | **bool** |  | [optional] 
**virtualization_realm** | [**MinimalVirtualizationRealm**](MinimalVirtualizationRealm.md) |  | [optional] 
**deployment_run_result_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


