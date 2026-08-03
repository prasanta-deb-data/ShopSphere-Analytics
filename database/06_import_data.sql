/*
=========================================================
ShopSphere Analytics
06_import_data.sql

Bulk Import CSV Files
=========================================================
*/

USE ShopSphereAnalytics;
GO

EXEC sp_configure 'show advanced options',1;
RECONFIGURE;

EXEC sp_configure 'Ad Hoc Distributed Queries',1;
RECONFIGURE;
GO

BULK INSERT States
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\states.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Cities
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\cities.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Categories
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\categories.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT SubCategories
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\subcategories.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Brands
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\brands.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Suppliers
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\suppliers.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Warehouses
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\warehouses.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT PaymentMethods
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\payment_methods.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Couriers
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\couriers.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT ReturnReasons
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\return_reasons.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT SupportIssues
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\support_issues.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT FestivalCalendar
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\festival_calendar.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

BULK INSERT Calendar
FROM 'C:\Portfolio\ShopSphere-Analytics\output\csv\calendar.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='0x0A',
CODEPAGE='65001',
TABLOCK
);
GO

