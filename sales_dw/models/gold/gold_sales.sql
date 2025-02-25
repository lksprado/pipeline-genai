with 
bronze as (
    select 
    *
    from {{ref('silver_sales') }} 
)
select 
t.product,
sum(t.value) as values,
sum(t.quantity) as counts,
sum(t.value)/sum(t.quantity) as ticket_medio
from bronze t 
group by 
t.product