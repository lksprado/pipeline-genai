with 
bronze as (
    select 
    *
    from {{ref('bronze_sales') }} 
)
select 
*
from bronze t 
where t.created_at >= current_date -7