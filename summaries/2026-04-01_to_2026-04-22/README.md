# Iceberg Community Sync Summary

- Period: `2026-04-01` to before `2026-04-22`
- Review candidates: `20`

## apache/iceberg

### Java

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
- Core: Expose MetricsConfig.from method with 3-parameter version (#15819) (Thanks Yuya Ebihara!)
- API: Relax partition name check when source column is dropped (#15967) (Thanks Russell Spitzer!)
- AWS: Add proxy system property and environment variable configuration for HTTP clients (#15506) (Thanks Mervyn Lobo!)
- API: Fix TableIdentifier.toLowerCase to use Locale.ROOT for namespace levels (#15956) (#15958) (Thanks Govindarajan!)
- Docs: Add Hive Metastore schema validation warnings for schema evolution with Hive catalog (#15814) (Thanks jackylee, Copilot, and Manu Zhang!)
- Flink: Fix checkArgument message for flink streaming (#15907) (Thanks genxiong7!)
- Core: Fix StructLikeWrapper.equals exception with mismatched partition types (#15945) (Thanks Yuya Ebihara!)
- Hive encryption nits (#14659) (Thanks Sreesh Maheshwar and Claude Opus 4.6 (1M context)!)
- AWS, Core: Switch Jetty to use new Compression API for GZIP (#15043) (Thanks Eduard Tudenhoefner!)
