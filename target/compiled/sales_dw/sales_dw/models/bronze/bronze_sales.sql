with source as (
        select * from "postgres"."dw_lcs"."sales"
  ),
renamed as (
    select
    *
    from source
)
select * from renamed