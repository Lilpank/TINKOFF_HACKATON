session_id="$1"
command_1_id="$2"
command_1_image="$3"
command_1_port=8081
command_1_pass="$4"
mediator="http://mediator:8080"

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
