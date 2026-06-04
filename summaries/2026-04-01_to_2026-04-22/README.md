# Iceberg Community Sync Summary

- Period: `2026-04-01` to before `2026-04-22`
- Review candidates: `186`

## apache/iceberg

### Java

_Top 20 of 71 scored commits._

- Core: Add fromId to EntryStatus and ManifestEntry.Status (#15983) (Thanks Anoop Johnson!)
- Core: Introduce default values in RESTCatalogProperties (#15873) (Thanks gaborkaszab!)
- Flink: Add passthroughRecords option to DynamicIcebergSink (#15433) (Thanks Han You and Jordan Epstein!)
- Core, API, Spark: Add FileContent.fromId (#15953) (Thanks Anoop Johnson!)
- Flink: Backport add passthroughRecords option to DynamicIcebergSink (#16019) (Thanks Han You!)
- Core: Expose HostnameVerificationPolicy in TLSConfigurer (#15500) (Thanks Alexandre Dutra!)
- Spec: Add 404 response for config endpoint (#15746) (Thanks Oguzhan Unlu!)
- Spark (4.0, 3.5): Set data file sort_order_id in manifest for writes from Spark (#15832) (Thanks jbewing!)
- AWS: Add chunked encoding configuration for S3 requests (#15242) (Thanks Jiajia Li!)
- API, Core: Move stats classes to core as package-private (#15971) (Thanks Eduard Tudenhoefner!)
- Parquet: Fix NPE in ParquetAvroWriter when schema contains variant type (#15934) (Thanks Neelesh Salian!)
- Docs: Add Hive Metastore schema validation warnings for schema evolution with Hive catalog (#15814) (Thanks jackylee, Copilot, and Manu Zhang!)
- Core: Expose MetricsConfig.from method with 3-parameter version (#15819) (Thanks Yuya Ebihara!)
- API: Relax partition name check when source column is dropped (#15967) (Thanks Russell Spitzer!)
- AWS: Add proxy system property and environment variable configuration for HTTP clients (#15506) (Thanks Mervyn Lobo!)
- API: Fix TableIdentifier.toLowerCase to use Locale.ROOT for namespace levels (#15956) (#15958) (Thanks Govindarajan!)
- Flink: Fix checkArgument message for flink streaming (#15907) (Thanks genxiong7!)
- Core: Fix StructLikeWrapper.equals exception with mismatched partition types (#15945) (Thanks Yuya Ebihara!)
- Hive encryption nits (#14659) (Thanks Sreesh Maheshwar and Claude Opus 4.6 (1M context)!)
- AWS, Core: Switch Jetty to use new Compression API for GZIP (#15043) (Thanks Eduard Tudenhoefner!)

## apache/iceberg-python

### Python

_Top 20 of 24 scored commits._

- Fix ManifestEntry.snapshot_id setter writing to wrong index (#3257) (Thanks Sotaro Hikita!)
- fix: Handle optional properties in load namespace properties response (#3169) (Thanks geruh!)
- fix zizmor ci issue by bumping codeql-action to v4.35.2 (#3245) (Thanks geruh!)
- Fix pa.Schema type annotations in schema_to_pyarrow (#3261) (Thanks David Zhao!)
- ci: fix zizmor workflow (#3243) (Thanks Kevin Liu!)
- CI: Lock REST Fixture to 1.10.1 (#3240) (Thanks Fokko Driesprong!)
- Build: Bump pytest from 9.0.2 to 9.0.3 (#3238) (Thanks dependabot[bot]!)
- Build: Bump nbconvert from 7.17.0 to 7.17.1 (#3262) (Thanks dependabot[bot]!)
- Build: Bump boto3 from 1.40.61 to 1.42.84 (#3226) (Thanks dependabot[bot]!)
- Build: Bump bodo from 2026.2 to 2026.4 (#3253) (Thanks dependabot[bot]!)
- Build: Bump adlfs from 2026.2.0 to 2026.4.0 (#3252) (Thanks dependabot[bot]!)
- Build: Bump s3fs from 2026.2.0 to 2026.3.0 (#3251) (Thanks dependabot[bot]!)
- Build: Bump google-auth from 2.49.1 to 2.49.2 (#3250) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.9.2 to 1.10.1 (#3249) (Thanks dependabot[bot]!)
- Build: Bump requests from 2.33.0 to 2.33.1 (#3227) (Thanks dependabot[bot]!)
- Build: Bump google-cloud-bigquery from 3.40.1 to 3.41.0 (#3228) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.8.0 to 1.9.0 (#3229) (Thanks dependabot[bot]!)
- Build: Bump sqlalchemy from 2.0.48 to 2.0.49 (#3230) (Thanks dependabot[bot]!)
- Build: Bump click from 8.3.1 to 8.3.2 (#3231) (Thanks dependabot[bot]!)
- Build: Bump daft from 0.6.14 to 0.7.7 (#3232) (Thanks dependabot[bot]!)

## apache/iceberg-rust

### Rust

_Top 20 of 23 scored commits._

- feat(encryption) [2/N] Support encryption: Add streaming encryption/decryption (#2286) (Thanks Xander!)
- refactor(storage): remove the configured_scheme parameter from storage impls (#2338) (Thanks R. Conner Howell!)
- tests(s3tables): add s3tables end-to-end test to verify table creation/loading plus reading/writing (#2315) (Thanks Daniel Carl Jones!)
- fix: build_fallback_field_id_map produces incorrect column indices for schemas with nested types (#2307) (Thanks Matt Butrovich and blackmwk!)
- fix(storage/s3): default to virtual-host-style addressing (#2330) (Thanks Jiajia Li!)
- fix: incorrect Parquet INT96 timestamp values from ArrowReader (#2301) (Thanks Matt Butrovich!)
- fix(s3tables): use 's3' as the default scheme (#2313) (Thanks R. Conner Howell!)
- support fixedbinary(n) (#2348) (Thanks jeff-sqds!)
- Fix RUSTSEC-2026-0097 (#2331) (Thanks blackmwk!)
- chore: update comment tag to match the exact version to fix zizmor (#2333) (Thanks Shawn Chang!)
- Fix zizmor workflow (#2324) (Thanks blackmwk!)
- ci: fix zizmor workflow (#2334) (Thanks Kevin Liu!)
- Fix ci workflow failure (#2325) (Thanks blackmwk!)
- chore: bump datafusion to 53.1.0 (#2350) (Thanks Xander!)
- chore(deps): Bump rustls-webpki from 0.103.10 to 0.103.12 in /bindings/python (#2352) (Thanks dependabot[bot]!)
- chore(deps): Bump actions/upload-artifact from 7.0.0 to 7.0.1 (#2345) (Thanks dependabot[bot]!)
- chore(deps): Bump PyO3/maturin-action from 1.50.1 to 1.51.0 (#2346) (Thanks dependabot[bot]!)
- chore(deps): Bump minijinja from 2.18.0 to 2.19.0 (#2322) (Thanks dependabot[bot]!)
- chore(deps): Bump tokio from 1.50.0 to 1.51.0 (#2321) (Thanks dependabot[bot]!)
- chore(deps): Bump astral-sh/setup-uv from 7.3.1 to 8.0.0 (#2314) (Thanks dependabot[bot] and Shawn Chang!)

## apache/iceberg-go

### Go

_Top 20 of 58 scored commits._

- feat(table): Add support for row lineage in v3 (#735) (Thanks Dao Thanh Tung!)
- feat(table): add bin-pack compaction strategy (#850) (Thanks Andrei Tserakhau!)
- feat(table): add RewriteDataFiles for compaction execution (#892) (Thanks Andrei Tserakhau!)
- feat(table): support delete file removal in overwrite commits (#851) (Thanks Andrei Tserakhau!)
- feat(cli): add compact analyze and compact run commands (#903) (Thanks Andrei Tserakhau!)
- perf(table): Add optional skip duplicate check on AddDataFiles (#901) (Thanks Abhi Rathod!)
- feat(table): classify deletion vectors in scan planning (#855) (Thanks Andrei Tserakhau!)
- feat(table): retry doCommit on commit-conflict errors (#830) (#912) (Thanks Andrei Tserakhau!)
- feat(compaction): add Analyze for dry-run compaction planning (#893) (Thanks Andrei Tserakhau!)
- feat(catalog): add `WithOAuthTLSConfig` for separate OAuth server TLS (#895) (Thanks Lovro Mažgon!)
- fix(table): populate WriteTask.SortOrderID in data file writers (#875) (Thanks Ali Asghar!)
- fix(table): prune StatisticsList and PartitionStatsList in RemoveSnapshots (#873) (Thanks Ali Asghar!)
- fix: decode pre-1.4 Java Iceberg legacy manifest list field names (#889) (#890) (Thanks Tanmay Rauth!)
- feat(table)!: multi-arg transforms in partition and sort fields (#824) (Thanks Andrei Tserakhau!)
- feat(#492): implement SetStatistics, RemoveStatistics, AddEncryptionKey, RemoveEncryptionKey updates (#902) (Thanks Tanmay Rauth and Matt Topol!)
- bench(table): read-perf degradation under equality delete pressure (#852) (Thanks Andrei Tserakhau!)
- fix(table): warn on row count mismatch in Overwrite (#894) (Thanks Andrei Tserakhau!)
- feat(table): add snapshot ancestry utility (#911) (Thanks Andrei Tserakhau!)
- fix(table): fast-append must inherit all parent manifests unconditionally (#869) (Thanks cassio-paesleme!)
- fix(table): delete statistics files in ExpireSnapshots PostCommit #837 (#882) (Thanks Tanmay Rauth!)

## apache/iceberg-cpp

### C++

_Top 10 of 10 scored commits._

- feat(puffin): add format constants, utilities, and JSON serde (#603) (Thanks ZhaoXuan!)
- feat: add s3 file io integration (#548) (Thanks liuxiaoyu!)
- feat(data): add DeleteLoader for position and equality delete files (#610) (Thanks Gang Wu!)
- feat(rest): support namespace separator (#617) (Thanks Gang Wu!)
- feat: implement incremental changelog scan (#611) (Thanks wzhuo!)
- chore: add more ai related .gitignore (#621) (Thanks Zehua Zou!)
- ci: apply github workflow best practice (zizmor/codeql/asf-allowlist-check) (#618) (Thanks Kevin Liu!)
- ci: set zizmor min-severity and min-confidence to medium (#620) (Thanks Kevin Liu!)
- feat(perf): optimize AddRange in RoaringPositionBitmap (#608) (Thanks Sebastian Baunsgaard!)
- chore(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 (#622) (Thanks dependabot[bot]!)
