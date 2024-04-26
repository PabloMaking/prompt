# CloudFunctions-GoogleApis

## CloudFunction

| Name                                                    | Location     | State  | Runtime   | Memory(MiB) | Timeout | ServiceAccount                |
| :-----------------------------------------------------: | :----------: | :----: | :-------: | :---------: | :-----: | :---------------------------: |
| anonimize                                               | europe-west1 | ACTIVE | python311 | 128         | 0:02:00 | anonimize                     |
| autos-price-ranking--call-endpoint                      | europe-west1 | ACTIVE | python39  | 256         | 0:01:00 | autos-price-ranking--sa       |
| cross-scheduler-cf                                      | europe-west1 | ACTIVE | python312 | 128         | 0:03:00 | cross-schedulers              |
| mapfre-dig-esp--dat--bq_check_event_tables              | europe-west1 | ACTIVE | python312 | 256         | 0:02:00 | bq-check-event-tables         |
| mapfre-dig-esp--dat--cf_dataflow_cancel_long_batch_jobs | europe-west1 | ACTIVE | python312 | 128         | 0:09:00 | dataflow-cancel-batch-jobs-cf |
| mapfre-dig-esp--dat--reprocessing_events                | europe-west1 | ACTIVE | python312 | 256         | 0:09:00 | reprocessing-events           |
| mapfre-dig-esp--dat--scheduled_query_export_csv         | europe-west1 | ACTIVE | python312 | 512         | 0:09:00 | scheduled-query-export-csv    |
| markerting-cloud-sftp                                   | europe-west1 | ACTIVE | python311 | 1024        | 0:09:00 | markerting-cloud-sftp-cf      |
| sftp-gcs-rastreator                                     | europe-west1 | ACTIVE | python311 | 512         | 0:09:00 | sftp-gcs-rastreator-cf        |
| tecuidamos-auto-file                                    | europe-west1 | ACTIVE | python311 | 512         | 0:09:00 | tecuidamos-auto-file-cf       |