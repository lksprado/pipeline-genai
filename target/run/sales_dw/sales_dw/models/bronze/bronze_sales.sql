
  create view "postgres"."dw_lcs"."bronze_sales__dbt_tmp"
    
    
  as (
    with source as (
        select * from "postgres"."dw_lcs"."sales"
  ),
renamed as (
    select
    *
    from source
)
select * from renamed
  );