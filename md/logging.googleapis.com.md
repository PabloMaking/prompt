# Logging-GoogleApis

## LogBucket

| Name      | Description    | Location | State  |
| :-------: | :------------: | :------: | :----: |
| _Default  | Default bucket | global   | ACTIVE |
| _Required | Audit bucket   | global   | ACTIVE |

## LogMetric

| Name                      | Desciption                                            | Location |
| :-----------------------: | :---------------------------------------------------: | :------: |
| cloudrun-log-counter      | Null                                                  | global   |
| dashboard-template/metric | Custom metrics for MSD template monitoring dashboards | global   |
| k8s-error-metric          | Null                                                  | global   |

## LogSink

| Name                     | Desciption                                                                                                                                                | Location |
| :----------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :------: |
| _Default                 | Null                                                                                                                                                      | global   |
| _Required                | Null                                                                                                                                                      | global   |
| dataflow-logs-sink-Files | Routes in real time some specific logs from Dataflow that report the current state of the data sources being processed on Dataflow with the string [File: | global   |