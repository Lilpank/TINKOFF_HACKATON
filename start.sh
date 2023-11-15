session_id="$1"
command_1_id="$2"
command_1_image="$3"
command_1_port=8081
command_1_pass="$4"
mediator="http://mediator:8080"
command_2_id="$5"
command_2_image="$6"
command_2_port=8081
command_2_pass="$7"

docker run -d -t -i \
  -e SESSION_ID="$session_id" \
  -e BOT_URL="http://$command_1_id:${command_1_port}" \
  -e MEDIATOR_URL="$mediator" \
  -e BOT_ID="$command_1_id" \
  -e SERVER_PORT="${command_1_port}" \
  -e BOT_PASSWORD="${command_1_pass}" \
  --net internal \
  --name "$command_1_id" \
  "$command_1_image" &

sleep 1

docker run -d -t -i \
  -e SESSION_ID="$session_id" \
  -e BOT_URL="http://$command_2_id:${command_2_port}" \
  -e MEDIATOR_URL="$mediator" \
  -e BOT_ID="$command_2_id" \
  -e SERVER_PORT="${command_2_port}" \
  -e BOT_PASSWORD="${command_2_pass}" \
  --net internal \
  --name "$command_2_id" \
  "$command_2_image" &
