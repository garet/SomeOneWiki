<html>
<head>
<title></title>
<meta content="">

<style>
    body{
	margin: 0;
	padding: 0;
    }
    
    .body{
	background-color: #a1a1a1;
	
	width: 100%;
	min-height: 800px;
    }
    .header{
	background-color: #999999;
	
	display: block;
	height: 100px;
    }
    .center{
	background-color: #aaaaaa;
	
	display: block;
	height: 640px;
    }
    .footer{
	background-color: #999999;
	
	display: block;
	height: 100px;
    }
</style>
</head>


<body>
    <div class="body">
	<div class="header">
	    {{ data1.Apt() }}
	</div>
	<div class="center">
	    {{ data2['center'] }}
	</div>
	<div class="footer">
	    Footer
	</div>
    </div>
</body>
</html>