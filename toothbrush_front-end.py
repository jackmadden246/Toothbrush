<html>
<head>
<title> Insights regarding the Toothbrush project</title>
<style>
            #p {
                background-color: white;
            }
            #h1 {
                background-color: red;
            }
            #h2 {
                background-color: red;
            }
           #h3 {
                background-color: blue;
            }
        </style>
</head>
<body style = "background-color:orange;">
<h1>MariaDB insights regarding the Toothbrush project</h1>
<?php
include_once('../../database_conn.php');
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
}

?>
<h2 id = "h2"> Top insights which concern the database table that contains all toothbrush orders</h2>
<p id = "p"> From the insights gathered, the latitude and longitude were analysed for information about potential areas that toothbrush sales could be generated. Have a look at some of our findings below:
<?php

$sql = "SELECT max(latitude) as highest_latitude, max(longitude) as highest_longitude, min(longitude) as lowest_longitude, min(latitude) as lowest_latitude FROM Toothdata1.all_orders ";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
        while($row = mysqli_fetch_array($result)){
                echo "<br>";
                echo "1. The highest latitude that people have ordered toothbrushes from is " . $row['highest_latitude'] ;
                echo "<br>";
                echo "2. The highest longitude that people have ordered toothbrushes from is " . $row['highest_longitude'];
}
}
?>
<p id = "p"> Did you know that if the person who brought a toothbrush at the highest latitude was the same person who brought the a toothbrush at the highest longitude, they would live in the North Sea? See below:</p>
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2084.5264443697743!2d1.68606731599524!3d58.50249098137721!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xa6d09e68d3d3853d!2zNTjCsDMwJzA5LjAiTiAxwrA0MScxNy43IkU!5e0!3m2!1sen!2suk!4v1671728227462!5m2!1sen!2suk" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
<p id = "p"> If those insights were not enough to dazzle your mind, here are some more below:
<?php
$sql = "SELECT max(latitude) as highest_latitude, max(longitude) as highest_longitude, min(longitude) as lowest_longitude, min(latitude) as lowest_latitude FROM Toothdata1.all_orders ";
$result = $conn->query($sql);
        while($row = mysqli_fetch_array($result)){
                echo "<br>";
                echo "3. The lowest latitude that people have ordered toothbrushes from is " . $row['lowest_latitude'];
                echo "<br>";
                echo "4. The lowest longitude that people have ordered toothbrushes from is " . $row['lowest_longitude'];
}
?>
<p id = "p"> Please see below for what happens if you are the lucky person who resides at the lowest latitude and longitude:</p>
<a href = "https://goo.gl/maps/fkhB8GKHRdQn8pUC7"> If you input the minimum latitude and longitude together, the result is the North Atlantic Ocean!!</a>

<h2 id = "h2"> Top insights about the database table that has the null toothbrush orders</h2>
<p id = "p"> The null table can provide valuable insights about the age range of the customers who did not get thir orders delivered, and the size of those orders. Please see some of the insights below:

<?php
        $sql_1 = "SELECT min(Customer_Age) as youngest_null_customer, max(Customer_Age) as oldest_null_customer, min(Order_Quantity) as minimum_null_order_size, max(Order_Quantity) as maximum_null_order_size FROM Toothdata1.null_orders";
        $res = mysqli_query($conn,$sql_1);
        while( $row = mysqli_fetch_array($res)) {
                echo "<br>";
                echo "1. The age of the youngest customer to order a toothbrush but not receive it was " . $row['youngest_null_customer'];
                echo "<br>";
                echo "2. The age of the oldest customer to order a toothbrush is " . $row['oldest_null_customer'];
                echo "<br>";
                echo "3. The smallest order size of the toothbrushes that were not delivered is "  . $row['minimum_null_order_size'];
                echo "<br>";
                echo "4. The largest order size that have not been delivered is " . $row['maximum_null_order_size'];
}

?>

<h2 id = "h2"> Top insights gained from the  database table that has all of the current toothbrush orders</h2>
<p id = "p"> For those who did get their order delivered, here are some of the insights that have been uncovered:
<?php
        $sql_2 = "SELECT min(Customer_Age) as youngest_customer, max(Customer_Age) as oldest_customer, min(Order_Quantity) as minimum_order_size, max(Order_Quantity) as maximum_order_size FROM Toothdata1.current_orders";
        $res1 = mysqli_query($conn,$sql_2);
        while($row = mysqli_fetch_array($res1)){
                echo "<br>";
                echo "1. The age of the youngest customer to order a toothbrush is " . $row['youngest_customer'];
                echo "<br>";
                echo "2. The age of the oldest customer to order a toothbrush is " . $row['oldest_customer'];
                echo "<br>";
                echo "3. The smallest order size is "  . $row['minimum_order_size']; 
 		    echo "<br>";
                echo "4. The largest order size is " . $row['maximum_order_size'];
}
$conn->close();
?>

</body>
</html>
                                                                                       1,4           Top
