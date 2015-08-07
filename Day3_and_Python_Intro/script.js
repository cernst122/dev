console.log("hey there");

$(document).ready(
  function(){
    $("#insert_button").click(createListElement); //when the button is pressed, do something: click
  }
)

function createListElement(){
  var person=$("#assignee").val();
  var task=$("#new_task").val();
  $("#task_list").append("<li>" + person + "  " + task + "</li>"); //adds person and task to list
}
