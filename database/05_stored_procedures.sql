/*
=========================================================
ShopSphere Analytics
05_stored_procedures.sql

Business Stored Procedures
=========================================================
*/

USE ShopSphereAnalytics;
GO

/*
=========================================================
Top Selling Products
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_TopSellingProducts
(
    @Top INT = 10
)
AS
BEGIN

SET NOCOUNT ON;

SELECT TOP (@Top)

p.ProductID,
p.ProductName,

SUM(oi.Quantity) QuantitySold,

SUM(oi.TotalPrice) Revenue

FROM Products p

INNER JOIN OrderItems oi
ON p.ProductID=oi.ProductID

GROUP BY

p.ProductID,
p.ProductName

ORDER BY Revenue DESC;

END
GO

/*
=========================================================
Monthly Sales
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_MonthlySales
(
    @Year INT
)
AS
BEGIN

SET NOCOUNT ON;

SELECT

MONTH(OrderDate) MonthNo,

DATENAME(MONTH,OrderDate) MonthName,

COUNT(*) Orders,

SUM(FinalAmount) Revenue

FROM Orders

WHERE YEAR(OrderDate)=@Year

GROUP BY

MONTH(OrderDate),

DATENAME(MONTH,OrderDate)

ORDER BY MonthNo;

END
GO

/*
=========================================================
Customer Purchase History
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_CustomerPurchaseHistory
(
    @CustomerID INT
)
AS
BEGIN

SET NOCOUNT ON;

SELECT

o.OrderID,

o.OrderDate,

o.FinalAmount,

o.OrderStatus,

o.PaymentStatus

FROM Orders o

WHERE CustomerID=@CustomerID

ORDER BY OrderDate DESC;

END
GO

/*
=========================================================
Customer Lifetime Value
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_CustomerLifetimeValue
AS
BEGIN

SET NOCOUNT ON;

SELECT

c.CustomerID,

CONCAT(c.FirstName,' ',c.LastName) CustomerName,

COUNT(o.OrderID) TotalOrders,

SUM(o.FinalAmount) LifetimeValue,

AVG(o.FinalAmount) AverageOrderValue

FROM Customers c

LEFT JOIN Orders o

ON c.CustomerID=o.CustomerID

GROUP BY

c.CustomerID,

c.FirstName,

c.LastName

ORDER BY LifetimeValue DESC;

END
GO

/*
=========================================================
Low Stock Products
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_LowStockProducts
AS
BEGIN

SET NOCOUNT ON;

SELECT

p.ProductID,

p.ProductName,

w.WarehouseName,

i.StockQuantity,

i.ReorderLevel

FROM Inventory i

INNER JOIN Products p

ON i.ProductID=p.ProductID

INNER JOIN Warehouses w

ON i.WarehouseID=w.WarehouseID

WHERE i.StockQuantity<=i.ReorderLevel

ORDER BY i.StockQuantity;

END
GO


/*
=========================================================
Product Performance
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_ProductPerformance
(
    @ProductID INT
)
AS
BEGIN

SET NOCOUNT ON;

SELECT

p.ProductName,

SUM(oi.Quantity) QuantitySold,

SUM(oi.TotalPrice) Revenue,

AVG(r.Rating) AverageRating

FROM Products p

LEFT JOIN OrderItems oi

ON p.ProductID=oi.ProductID

LEFT JOIN Reviews r

ON p.ProductID=r.ProductID

WHERE p.ProductID=@ProductID

GROUP BY

p.ProductName;

END
GO

/*
=========================================================
Revenue by State
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_RevenueByState
AS
BEGIN

SET NOCOUNT ON;

SELECT

s.StateName,

SUM(o.FinalAmount) Revenue

FROM Orders o

INNER JOIN Customers c
ON o.CustomerID=c.CustomerID

INNER JOIN CustomerAddresses ca
ON c.CustomerID=ca.CustomerID
AND ca.IsDefault=1

INNER JOIN Cities ct
ON ca.CityID=ct.CityID

INNER JOIN States s
ON ct.StateID=s.StateID

GROUP BY

s.StateName

ORDER BY Revenue DESC;

END
GO

/*
=========================================================
Shipment Performance
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_ShipmentPerformance
AS
BEGIN

SET NOCOUNT ON;

SELECT

c.CourierName,

COUNT(*) Shipments,

AVG(DATEDIFF(DAY,ShippingDate,DeliveredDate))
AverageDeliveryDays

FROM Shipments s

INNER JOIN Couriers c

ON s.CourierID=c.CourierID

GROUP BY

c.CourierName;

END
GO

/*
=========================================================
Return Analysis
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_ReturnAnalysis
AS
BEGIN

SET NOCOUNT ON;

SELECT

rr.ReturnReasonName,

COUNT(*) TotalReturns,

SUM(r.RefundAmount) RefundAmount

FROM Returns r

INNER JOIN ReturnReasons rr

ON r.ReturnReasonID=rr.ReturnReasonID

GROUP BY

rr.ReturnReasonName

ORDER BY TotalReturns DESC;

END
GO

/*
=========================================================
Coupon Performance
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_CouponPerformance
AS
BEGIN

SET NOCOUNT ON;

SELECT

c.CouponCode,

COUNT(oc.OrderCouponID) TimesUsed,

SUM(oc.DiscountAmount) TotalDiscount

FROM Coupons c

LEFT JOIN OrderCoupons oc

ON c.CouponID=oc.CouponID

GROUP BY

c.CouponCode

ORDER BY TimesUsed DESC;

END
GO

/*
=========================================================
Website Conversion
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_WebsiteConversion
AS
BEGIN

SET NOCOUNT ON;

SELECT

TrafficSource,

COUNT(*) Sessions,

SUM(CASE WHEN Converted=1 THEN 1 ELSE 0 END)
Conversions,

ROUND(

100.0*

SUM(CASE WHEN Converted=1 THEN 1 ELSE 0 END)

/COUNT(*)

,2) ConversionRate

FROM WebsiteTraffic

GROUP BY

TrafficSource;

END
GO

/*
=========================================================
Sales Dashboard
=========================================================
*/

CREATE OR ALTER PROCEDURE usp_SalesDashboard
AS
BEGIN

SET NOCOUNT ON;

SELECT

COUNT(*) Orders,

SUM(FinalAmount) Revenue,

AVG(FinalAmount) AverageOrderValue,

MAX(FinalAmount) HighestOrder

FROM Orders;

END
GO

/*
=========================================================
Customer Dashboard
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_CustomerDashboard
AS
BEGIN

SET NOCOUNT ON;

SELECT

COUNT(*) Customers,

SUM(CASE WHEN IsActive=1 THEN 1 ELSE 0 END)
ActiveCustomers,

AVG(LoyaltyPoints)
AverageLoyaltyPoints

FROM Customers;

END
GO

/*
=========================================================
Inventory Dashboard
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_InventoryDashboard
AS
BEGIN

SET NOCOUNT ON;

SELECT

COUNT(*) Products,

SUM(StockQuantity) TotalStock,

AVG(StockQuantity) AverageStock

FROM Inventory;

END
GO

/*
=========================================================
Executive Dashboard
=========================================================
*/
CREATE OR ALTER PROCEDURE usp_ExecutiveDashboard
AS
BEGIN

SET NOCOUNT ON;

SELECT

(SELECT COUNT(*) FROM Customers) Customers,

(SELECT COUNT(*) FROM Orders) Orders,

(SELECT SUM(FinalAmount) FROM Orders) Revenue,

(SELECT COUNT(*) FROM Products) Products,

(SELECT COUNT(*) FROM Returns) Returns,

(SELECT COUNT(*) FROM SupportTickets) Tickets;

END
GO
