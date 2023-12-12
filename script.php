<?php
$json = file_get_contents("php://input");
$data = json_decode($json, true);

$str = array_map(function($value){
	return $value;
}, $data);

$str = implode(",",$str);

$output = shell_exec("python script.py " . json_encode($str));
print_r($output);
?>