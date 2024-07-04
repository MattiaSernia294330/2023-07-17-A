from database.DB_connect import DBConnect
from model.Product import Product



class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getColor():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Product_color 
from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getNodi(colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
from go_products gp
where gp.Product_color =%s"""

        cursor.execute(query,(colore,))

        for row in cursor:
            result.append(Product(row["Product_number"],row["Product"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi(anno,colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds.Product_number as p1, gds2.Product_number as p2, count(DISTINCT gds2.`Date`) as peso
from go_daily_sales gds 
join go_daily_sales gds2 on gds.`Date`=gds2.`Date`
join go_products gp on gds.Product_number = gp.Product_number 
join go_products gp2 on gds2.Product_number = gp2.Product_number 
where gp.Product_number < gp2.Product_number and year(gds2.`Date`)=%s and gp.Product_color =gp2.Product_color and gp2.Product_color =%s and gds.Retailer_code=gds2.Retailer_code 
group by gds.Product_number, gds2.Product_number"""

        cursor.execute(query, (anno,colore))

        for row in cursor:
            result.append((row["p1"], row["p2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


