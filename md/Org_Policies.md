# Organization Policies

| Name                                                                                                 | Action |
| :--------------------------------------------------------------------------------------------------: | :----: |
| Define access mode for Vertex AI Workbench notebooks and instances                                   | ALLOW  |
| Disable file downloads on new Vertex AI Workbench instances                                          | ALLOW  |
| Disable root access on new Vertex AI Workbench user-managed notebooks and instances                  | ALLOW  |
| Disable terminal on new Vertex AI Workbench instances                                                | ALLOW  |
| Restrict environment options on new Vertex AI Workbench notebooks and instances                      | ALLOW  |
| Require automatic scheduled upgrades on new Vertex AI Workbench user-managed notebooks and instances | ALLOW  |
| Restrict VPC networks on new Vertex AI Workbench instances                                           | ALLOW  |
| Restrict public IP access on new Vertex AI Workbench notebooks and instances                         | ALLOW  |
| Disable Source Code Download                                                                         | ALLOW  |
| Runtime Deployment Exemption (App Engine)                                                            | DENY   |
| Disable BigQuery Omni for Cloud AWS                                                                  | ALLOW  |
| Disable BigQuery Omni for Cloud Azure                                                                | ALLOW  |
| Allowed Integrations (Cloud Build)                                                                   | ALLOW  |
| Allowed Worker Pools (Cloud Build)                                                                   | ALLOW  |
| Disable Create Default Service Account (Cloud Build)                                                 | DENY   |
| Disable Cloud Deploy service labels                                                                  | ALLOW  |
| Allowed Cloud Functions Generations                                                                  | ALLOW  |
| Allowed VPC Connector egress settings (Cloud Functions)                                              | ALLOW  |
| Allowed ingress settings (Cloud Functions)                                                           | ALLOW  |
| Require VPC Connector (Cloud Functions)                                                              | ALLOW  |
| Restrict which KMS CryptoKey types may be created.                                                   | ALLOW  |
| Minimum destroy scheduled duration per key                                                           | ALLOW  |
| Restrict key destruction to disabled key versions                                                    | ALLOW  |
| Allowed VLAN Attachment encryption settings                                                          | ALLOW  |
| Disable VM nested virtualization                                                                     | ALLOW  |
| Disable VM serial port logging to Stackdriver                                                        | ALLOW  |
| Disable VM serial port access                                                                        | ALLOW  |
| Disable Global Access to VM Serial Ports                                                             | ALLOW  |
| Disable Instance Data Access APIs                                                                    | ALLOW  |
| Disable Guest Attributes of Compute Engine metadata                                                  | ALLOW  |
| Restrict shared VPC project lien removal                                                             | ALLOW  |
| Require OS Login                                                                                     | ALLOW  |
| Shielded VMs                                                                                         | ALLOW  |
| Restrict Non-Confidential Computing                                                                  | ALLOW  |
| Sets the internal DNS setting for new projects to Zonal DNS Only                                     | ALLOW  |
| Compute Storage resource use restrictions (Compute Engine disks, images, and snapshots)              | ALLOW  |
| Define trusted image projects                                                                        | ALLOW  |
| Define allowed external IPs for VM instances                                                         | ALLOW  |
| Disable diagnostic administrative access pathways in GKE.                                            | ALLOW  |
| Domain restricted contacts                                                                           | ALLOW  |
| Disable Project Security Contacts                                                                    | ALLOW  |
| Google Cloud Platform - Resource Location Restriction                                                | ALLOW  |
| Restrict which projects may supply KMS CryptoKeys for CMEK                                           | ALLOW  |
| Restrict which services may create resources without CMEK                                            | ALLOW  |
| Domain restricted sharing                                                                            | ALLOW  |
| Disable Audit Logging exemption                                                                      | ALLOW  |
| Disable Service Account Key Upload                                                                   | ALLOW  |
| Disable service account creation                                                                     | ALLOW  |
| Disable service account key creation                                                                 | ALLOW  |
| Disable Cross-Project Service Account Usage                                                          | DENY   |
| Restrict removal of Cross Project Service Account liens                                              | ALLOW  |
| Disable Automatic IAM Grants for Default Service Accounts                                            | ALLOW  |
| Allow extending lifetime of OAuth 2.0 access tokens to up to 12 hours                                | DENY   |
| Allowed Destinations for Exporting Resources                                                         | DENY   |
| Allowed Sources for Importing Resources                                                              | DENY   |
| Require Enabled Services Allow List for Cross-Organization Move                                      | DENY   |
| Allowed ingress settings (Cloud Run)                                                                 | ALLOW  |
| Allowed VPC egress settings (Cloud Run)                                                              | ALLOW  |
| Allowed Binary Authorization Policies (Cloud Run)                                                    | ALLOW  |
| Restrict allowed Google Cloud APIs and services                                                      | ALLOW  |
| Restrict Authorized Networks on Cloud SQL instances                                                  | ALLOW  |
| Restrict Public IP access on Cloud SQL instances                                                     | ALLOW  |
| Restrict non-compliant workloads for Cloud SQL instances.                                            | ALLOW  |
| Disable diagnostic and administrative access pathways in Cloud SQL to meet compliance requirements.  | ALLOW  |
| Enforce uniform bucket-level access                                                                  | ALLOW  |
| Retention policy duration in seconds                                                                 | ALLOW  |
| Cloud Storage - restrict authentication types                                                        | ALLOW  |
| Skip default network creation                                                                        | ALLOW  |
| Require SSL Policy                                                                                   | ALLOW  |
| Restrict VPC peering usage                                                                           | ALLOW  |
| Restrict Shared VPC Host Projects                                                                    | ALLOW  |
| Restrict Shared VPC Subnetworks                                                                      | ALLOW  |
| Restrict Shared VPC Backend Services                                                                 | ALLOW  |
| Restrict cross-project backend buckets and backend services                                          | ALLOW  |
| Restrict VPN Peer IPs                                                                                | ALLOW  |
| Restrict Load Balancer Creation Based on Load Balancer Types                                         | ALLOW  |
| Restrict Protocol Forwarding Based on type of IP Address                                             | ALLOW  |
| Restrict VM IP Forwarding                                                                            | ALLOW  |
| Restrict Dedicated Interconnect usage                                                                | ALLOW  |
| Restrict Partner Interconnect usage                                                                  | ALLOW  |
| Restrict Cloud NAT usage                                                                             | ALLOW  |
| Shared Reservations Owner Projects                                                                   | DENY   |
| Restrict Resource Service Usage                                                                      | ALLOW  |
| Restrict TLS Versions                                                                                | ALLOW  |
| Disable Workload Identity Cluster Creation                                                           | ALLOW  |
| Disable Internet Network Endpoint Groups                                                             | ALLOW  |
| Google Cloud Platform - Detailed Audit Logging Mode                                                  | ALLOW  |
| Disable Cloud Logging for Cloud Healthcare API                                                       | ALLOW  |
| Allowed external Identity Providers for workloads in Cloud IAM                                       | ALLOW  |
| Allowed AWS accounts that can be configured for workload identity federation in Cloud IAM            | ALLOW  |
| Restrict git remotes for repositories in Dataform                                                    | ALLOW  |
| Disable Private Service Connect for Consumers                                                        | ALLOW  |
| Restrict allowed Private Service Connect Consumers                                                   | ALLOW  |
| Restrict allowed Private Service Connect Producers                                                   | ALLOW  |
| Enforce Public Access Prevention                                                                     | ALLOW  |
| Restrict unencrypted HTTP access                                                                     | ALLOW  |
| Disable VPC Internal IPv6 usage                                                                      | ALLOW  |
| Disable Hybrid Cloud IPv6 usage                                                                      | ALLOW  |
| Disable VPC External IPv6 usage                                                                      | ALLOW  |
| Disable All IPv6 usage                                                                               | ALLOW  |
| Datastream - Block Public Connectivity Methods                                                       | ALLOW  |
| Allowed target types for jobs                                                                        | ALLOW  |
| Require predefined policies for VPC flow logs                                                        | ALLOW  |
| Require Firestore Service Agent for import/export                                                    | ALLOW  |
| Allowed VPC Service Controls mode for Anthos Service Mesh Managed Control Planes                     | ALLOW  |
| Enable settings required for compliance memory protection workloads                                  | ALLOW  |
| Disable Creation of Cloud Armor Security Policies                                                    | ALLOW  |
| Disable Creation of global self-managed SSL Certificates                                             | ALLOW  |
| Disable Enabling Identity-Aware Proxy (IAP) on global resources                                      | ALLOW  |
| Disable Enabling Identity-Aware Proxy (IAP) on regional resources                                    | ALLOW  |
| Disable Global Load Balancing                                                                        | ALLOW  |
| Disable SSH-in-browser                                                                               | ALLOW  |
| Service account key expiry duration in hours                                                         | ALLOW  |
| Restrict access on marketplace services                                                              | DENY   |
| Disable Public Marketplace                                                                           | ALLOW  |
| Enforce FIPS-compliant machine types                                                                 | ALLOW  |
| Enable advanced service control for compliance workloads                                             | ALLOW  |
| Disable Cloud Spanner multi-region if no location selected                                           | ALLOW  |
| Enforce in-transit regions for Pub/Sub messages                                                      | ALLOW  |
| Service account key exposure response                                                                | DENY   |