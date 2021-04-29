# nav-add-ons/web

## Installation

Copy the [extra code](etc) to the NAV config directory.

Apply the [patches](patches).

Update the NAV database:

```sql
alter table location alter column locationid type varchar;
alter table room alter column locationid type varchar;

alter table netbox alter column orgid type varchar;
alter table org alter column orgid type varchar;
alter table org alter column parent type varchar;
alter table vlan alter column orgid type varchar;

alter table cabling alter column roomid type varchar;
alter table netbox alter column roomid type varchar;
alter table room alter column roomid type varchar;

alter table usage alter column usageid type varchar;
alter table vlan alter column usageid type varchar;

alter table vendor alter column vendorid type varchar;
alter table type alter column vendorid type varchar;
```
