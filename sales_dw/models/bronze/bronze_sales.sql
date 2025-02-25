with source as (
        select * from {{ source('dw_lcs', 'sales') }}
  ),
renamed as (
    select
    *
    from source
)
select * from renamed