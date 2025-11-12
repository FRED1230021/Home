<?php
// signal.php
// Receive SDP or ICE candidates
$data = json_decode(file_get_contents("php://input"), true);
file_put_contents("signal_data.json", json_encode($data));
echo json_encode(["status" => "ok"]);
?>
