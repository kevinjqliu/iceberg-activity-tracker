# Iceberg Community Sync Summary

- Period: `2026-04-01` to before `2026-04-22`
- Review candidates: `186`

## apache/iceberg

### Java

_Top 20 themes from 71 scored commits._

- Core: Add fromId to EntryStatus and ManifestEntry.Status (#15983) (Thanks Anoop Johnson!)
- Core: Introduce default values in RESTCatalogProperties (#15873) (Thanks gaborkaszab!)
- Flink: Add passthroughRecords option to DynamicIcebergSink (#15433) (Thanks Han You and Jordan Epstein!)
- Core, API, Spark: Add FileContent.fromId (#15953) (Thanks Anoop Johnson!)
- Core: Expose HostnameVerificationPolicy in TLSConfigurer (#15500) (Thanks Alexandre Dutra!)
- Spec: Add 404 response for config endpoint (#15746) (Thanks Oguzhan Unlu!)
- Spark (4.0, 3.5): Set data file sort_order_id in manifest for writes from Spark (#15832) (Thanks jbewing!)
- AWS: Add chunked encoding configuration for S3 requests (#15242) (Thanks Jiajia Li!)
- API, Core: Move stats classes to core as package-private (#15971) (Thanks Eduard Tudenhoefner!)
- Parquet: Fix NPE in ParquetAvroWriter when schema contains variant type (#15934) (Thanks Neelesh Salian!)
- Core: Expose MetricsConfig.from method with 3-parameter version (#15819) (Thanks Yuya Ebihara!)
- API: Relax partition name check when source column is dropped (#15967) (Thanks Russell Spitzer!)
- AWS: Add proxy system property and environment variable configuration for HTTP clients (#15506) (Thanks Mervyn Lobo!)
- API: Fix TableIdentifier.toLowerCase to use Locale.ROOT for namespace levels (#15956) (#15958) (Thanks Govindarajan!)
- Flink: Fix checkArgument message for flink streaming (#15907) (Thanks genxiong7!)
- Core: Fix StructLikeWrapper.equals exception with mismatched partition types (#15945) (Thanks Yuya Ebihara!)
- Hive encryption nits (#14659) (Thanks Sreesh Maheshwar and Claude Opus 4.6 (1M context)!)
- AWS, Core: Switch Jetty to use new Compression API for GZIP (#15043) (Thanks Eduard Tudenhoefner!)
- Flink 2.1: Fix forward-writer chaining regression in DynamicIcebergSink (#16026) (Thanks drexler-sky!)
- API: Fix FileRange validation to reject negative offset/length (#15926) (Thanks Barry!)

## apache/iceberg-python

### Python

_Top 3 themes from 24 scored commits._

- Fix ManifestEntry.snapshot_id setter writing to wrong index (#3257) (Thanks Sotaro Hikita!)
- fix: Handle optional properties in load namespace properties response (#3169) (Thanks geruh!)
- Fix pa.Schema type annotations in schema_to_pyarrow (#3261) (Thanks David Zhao!)

## apache/iceberg-rust

### Rust

_Top 8 themes from 23 scored commits._

- feat(encryption) [2/N] Support encryption: Add streaming encryption/decryption (#2286) (Thanks Xander!)
- fix(storage/s3): default to virtual-host-style addressing (#2330) (Thanks Jiajia Li!)
- fix: build_fallback_field_id_map produces incorrect column indices for schemas with nested types (#2307) (Thanks Matt Butrovich and blackmwk!)
- fix: incorrect Parquet INT96 timestamp values from ArrowReader (#2301) (Thanks Matt Butrovich!)
- fix(s3tables): use 's3' as the default scheme (#2313) (Thanks R. Conner Howell!)
- refactor(storage): remove the configured_scheme parameter from storage impls (#2338) (Thanks R. Conner Howell!)
- support fixedbinary(n) (#2348) (Thanks jeff-sqds!)
- Fix RUSTSEC-2026-0097 (#2331) (Thanks blackmwk!)

## apache/iceberg-go

### Go

_Top 20 themes from 58 scored commits._

- Compaction and rewrite data files: expand rewrite planning and execution (#850, #851, #852, #892, #893, #901, #903) (Thanks Andrei Tserakhau and Abhi Rathod!)
- Row lineage: expand support for lineage-aware reads and writes (#735, #821) (Thanks Dao Thanh Tung and Andrei Tserakhau!)
- feat(table): classify deletion vectors in scan planning (#855) (Thanks Andrei Tserakhau!)
- feat(table): retry doCommit on commit-conflict errors (#830) (#912) (Thanks Andrei Tserakhau!)
- feat(catalog): add `WithOAuthTLSConfig` for separate OAuth server TLS (#895) (Thanks Lovro Mažgon!)
- fix(table): populate WriteTask.SortOrderID in data file writers (#875) (Thanks Ali Asghar!)
- fix(table): prune StatisticsList and PartitionStatsList in RemoveSnapshots (#873) (Thanks Ali Asghar!)
- feat(table)!: multi-arg transforms in partition and sort fields (#824) (Thanks Andrei Tserakhau!)
- feat(#492): implement SetStatistics, RemoveStatistics, AddEncryptionKey, RemoveEncryptionKey updates (#902) (Thanks Tanmay Rauth and Matt Topol!)
- fix(table): warn on row count mismatch in Overwrite (#894) (Thanks Andrei Tserakhau!)
- feat(table): add snapshot ancestry utility (#911) (Thanks Andrei Tserakhau!)
- fix(table): fast-append must inherit all parent manifests unconditionally (#869) (Thanks cassio-paesleme!)
- fix(table): delete statistics files in ExpireSnapshots PostCommit #837 (#882) (Thanks Tanmay Rauth!)
- fix: emit proper Avro fixed schema for FixedType partition columns (#845) (#881) (Thanks Tanmay Rauth!)
- fix(table): read retention table properties as defaults in ExpireSnapshots (#877) (Thanks Ali Asghar!)
- fix(rest): apply header.* additional props as HTTP headers on all requests (#921) (Thanks Ali Asghar!)
- feat(avro): replace hamba/avro with twmb/avro v1.5.0 (#871) (Thanks Travis Bischel and Claude Opus 4.6 (1M context)!)
- feat(table): support committing snapshots to branches other than main (#899) (Thanks Ali Asghar!)
- refactor(table): collapse DataFileStatistics.ToDataFile args into DataFileOpts (#888) (Thanks Ali Asghar!)
- feat(table): Add OpReplace to updateSnapshotSummaries (#853) (Thanks Dao Thanh Tung!)

## apache/iceberg-cpp

### C++

_Top 6 themes from 10 scored commits._

- feat: add s3 file io integration (#548) (Thanks liuxiaoyu!)
- feat(puffin): add format constants, utilities, and JSON serde (#603) (Thanks ZhaoXuan!)
- feat(data): add DeleteLoader for position and equality delete files (#610) (Thanks Gang Wu!)
- feat(rest): support namespace separator (#617) (Thanks Gang Wu!)
- feat: implement incremental changelog scan (#611) (Thanks wzhuo!)
- feat(perf): optimize AddRange in RoaringPositionBitmap (#608) (Thanks Sebastian Baunsgaard!)
