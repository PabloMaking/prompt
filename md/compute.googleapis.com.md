# Compute-GoogleApis

## Instance

| Name                                                 | MachineType      | Location       | State        | Network-Name | Subnetwork                                       | IP-Interna | Network-Tier | Network-Type   |
| :--------------------------------------------------: | :--------------: | :------------: | :----------: | :----------: | :----------------------------------------------: | :--------: | :----------: | :------------: |
| model-venus                                          | n1-standard-16   | europe-west1-b | ![](off.png) | external-nat | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.35 | PREMIUM      | ONE_TO_ONE_NAT |
| mapfre-dig-esp--dat--pro--autos-price-ranking--vm    | e2-standard-2    | europe-west1-b | ![](on.png)  | nic0         | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.26 | Null         | Null           |
| streaming-pro-mapfre-dig--04220246-9mhc-harness-qm3q | n1-standard-2    | europe-west1-c | ![](on.png)  | nic0         | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.7  | Null         | Null           |
| pro-mapfre-dig-trans--pub-04220247-ek66-harness-gz9v | e2-custom-1-5120 | europe-west1-d | ![](on.png)  | nic0         | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.11 | Null         | Null           |
| pro-mapfre-dig-trans--pub-04220247-ek66-harness-cctz | e2-custom-1-5120 | europe-west1-d | ![](on.png)  | nic0         | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.16 | Null         | Null           |