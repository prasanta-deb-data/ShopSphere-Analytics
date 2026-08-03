/*
=========================================================
ShopSphere Analytics
04_views.sql

Business Reporting Views
=========================================================
*/

USE ShopSphereAnalytics;
GO

/*
=========================================================
Sales Summary
=========================================================
*/

CREATE VIEW vw_SalesSummary
AS
SELECT

    o.OrderID,

    o.OrderDate,

    c.CustomerID,

    CONCAT(c.FirstName,' ',c.LastName) AS CustomerName,

    o.OrderStatus,

    o.PaymentStatus,

    o.OrderChannel,

    o.TotalAmount,

    o.DiscountAmount,

    o.TaxAmount,

    o.ShippingCharge,

    o.FinalAmount

FROM Orders o

INNER JOIN Customers c

ON o.CustomerID=c.CustomerID;
GO

/*
=========================================================
Product Sales
=========================================================
*/

CREATE VIEW vw_ProductSales
AS

SELECT

    p.ProductID,

    p.ProductName,

    b.BrandName,

    cat.CategoryName,

    SUM(oi.Quantity) AS TotalQuantitySold,

    SUM(oi.TotalPrice) AS Revenue,

    COUNT(DISTINCT oi.OrderID) AS TotalOrders

FROM Products p

INNER JOIN Brands b

ON p.BrandID=b.BrandID

INNER JOIN Categories cat

ON p.CategoryID=cat.CategoryID

INNER JOIN OrderItems oi

ON p.ProductID=oi.ProductID

GROUP BY

p.ProductID,

p.ProductName,

b.BrandName,

cat.CategoryName;
GO

/*
=========================================================
Customer KPI
=========================================================
*/

CREATE VIEW vw_CustomerKPI
AS

SELECT

c.CustomerID,

CONCAT(c.FirstName,' ',c.LastName) CustomerName,

COUNT(o.OrderID) TotalOrders,

SUM(o.FinalAmount) LifetimeValue,

AVG(o.FinalAmount) AverageOrderValue,

MAX(o.OrderDate) LastPurchaseDate

FROM Customers c

LEFT JOIN Orders o

ON c.CustomerID=o.CustomerID

GROUP BY

c.CustomerID,

c.FirstName,

c.LastName;
GO

/*
=========================================================
Inventory Status
=========================================================
*/

CREATE VIEW vw_InventoryStatus
AS

SELECT

p.ProductID,

p.ProductName,

w.WarehouseName,

i.StockQuantity,

i.ReservedQuantity,

i.ReorderLevel,

i.SafetyStock,

CASE

WHEN i.StockQuantity<=i.ReorderLevel

THEN 'Reorder Required'

ELSE 'Stock Available'

END InventoryStatus

FROM Inventory i

INNER JOIN Products p

ON i.ProductID=p.ProductID

INNER JOIN Warehouses w

ON i.WarehouseID=w.WarehouseID;
GO

/*
=========================================================
Payment Summary
=========================================================
*/

CREATE VIEW vw_PaymentSummary
AS

SELECT

PaymentStatus,

COUNT(*) TotalTransactions,

SUM(AmountPaid) TotalAmount

FROM Payments

GROUP BY

PaymentStatus;
GO

/*
=========================================================
Shipment Performance
=========================================================
*/

CREATE VIEW vw_ShipmentPerformance
AS

SELECT

co.CourierName,

COUNT(*) Shipments,

AVG(DATEDIFF(DAY,ShippingDate,DeliveredDate)) AvgDeliveryDays

FROM Shipments s

INNER JOIN Couriers co

ON s.CourierID=co.CourierID

GROUP BY

co.CourierName;
GO

/*
=========================================================
Product Ratings
=========================================================
*/

CREATE VIEW vw_ProductRatings
AS

SELECT

p.ProductID,

p.ProductName,

COUNT(r.ReviewID) TotalReviews,

AVG(CAST(r.Rating AS DECIMAL(5,2))) AverageRating

FROM Products p

LEFT JOIN Reviews r

ON p.ProductID=r.ProductID

GROUP BY

p.ProductID,

p.ProductName;
GO


/*
=========================================================
Return Analysis
=========================================================
*/

CREATE VIEW vw_ReturnAnalysis
AS

SELECT

rr.ReturnReasonName,

COUNT(*) TotalReturns,

SUM(r.RefundAmount) RefundAmount

FROM Returns r

INNER JOIN ReturnReasons rr

ON r.ReturnReasonID=rr.ReturnReasonID

GROUP BY

rr.ReturnReasonName;
GO


/*
=========================================================
Coupon Performance
=========================================================
*/

CREATE VIEW vw_CouponPerformance
AS

SELECT

c.CouponCode,

COUNT(oc.OrderCouponID) TimesUsed,

SUM(oc.DiscountAmount) TotalDiscount

FROM Coupons c

LEFT JOIN OrderCoupons oc

ON c.CouponID=oc.CouponID

GROUP BY

c.CouponCode;
GO

/*
=========================================================
Customer Support
=========================================================
*/

CREATE VIEW vw_SupportPerformance
AS

SELECT

TicketStatus,

Priority,

COUNT(*) Tickets,

AVG(DATEDIFF(HOUR,CreatedDate,ResolvedDate)) AvgResolutionHours

FROM SupportTickets

GROUP BY

TicketStatus,

Priority;
GO

/*
=========================================================
Website Analytics
=========================================================
*/

CREATE VIEW vw_WebsiteAnalytics
AS

SELECT

TrafficSource,

DeviceType,

COUNT(*) Sessions,

SUM(CASE WHEN Converted=1 THEN 1 ELSE 0 END) Conversions,

AVG(SessionDurationSeconds) AvgSessionDuration

FROM WebsiteTraffic

GROUP BY

TrafficSource,

DeviceType;
GO

/*
=========================================================
Monthly Sales
=========================================================
*/

CREATE VIEW vw_MonthlySales
AS

SELECT

YEAR(OrderDate) SalesYear,

MONTH(OrderDate) SalesMonth,

COUNT(*) Orders,

SUM(FinalAmount) Revenue

FROM Orders

GROUP BY

YEAR(OrderDate),

MONTH(OrderDate);
GO

/*
=========================================================
Daily Sales
=========================================================
*/

CREATE VIEW vw_DailySales
AS

SELECT

CAST(OrderDate AS DATE) SalesDate,

COUNT(*) Orders,

SUM(FinalAmount) Revenue

FROM Orders

GROUP BY

CAST(OrderDate AS DATE);
GO

/*
=========================================================
Top Customers
=========================================================
*/

CREATE VIEW vw_TopCustomers
AS

SELECT TOP 100

c.CustomerID,

CONCAT(c.FirstName,' ',c.LastName) CustomerName,

SUM(o.FinalAmount) Revenue

FROM Customers c

INNER JOIN Orders o

ON c.CustomerID=o.CustomerID

GROUP BY

c.CustomerID,

c.FirstName,

c.LastName

ORDER BY Revenue DESC;
GO

/*
=========================================================
Top Products
=========================================================
*/

CREATE VIEW vw_TopProducts
AS

SELECT TOP 100

p.ProductName,

SUM(oi.Quantity) QuantitySold,

SUM(oi.TotalPrice) Revenue

FROM Products p

INNER JOIN OrderItems oi

ON p.ProductID=oi.ProductID

GROUP BY

p.ProductName

ORDER BY Revenue DESC;
GO