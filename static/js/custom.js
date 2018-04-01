$('.delbutton').click(function(e){
  var id = e.target.id.split('_')[1];
  var pid = "#ans_"+id;
  var answer = confirm('Do you realy want to delete?');
  if(answer){
    //window.location = "/sp1/"+id+"/del_answer/";
    $.ajax({
        url:'/sp1/'+id+'/del_answer/',
        type: "GET",
        //data: {ans: newtext, csrfmiddlewaretoken: secur},
        //data: {},
        success:function(response){
          var secur = $("input[name = 'csrfmiddlewaretoken']").val();
          var topic = $(pid).parent().parent().attr('id').split('collapse')[1];
          //console.log('zzzzzz'+topic);
          newhtml = '<p class="alert alert-danger">Please write your answer below.</p>';
          newhtml += '<form action="/sp1/'+topic+'/set_answer/" method="post">';
          newhtml += '<input type="hidden" name="csrfmiddlewaretoken" value="'+secur+'">';
          newhtml += '<div class="form-group"><textarea name="ans" class="form-control" rows="4"></textarea></div>';
          newhtml += '<div class="text-right"><button type="submit" class="btn btn-primary">Save</button></div></form>';
          $(pid).html(newhtml);
          $('#ed_'+id).hide();
          $('#del_'+id).hide();
          $('#ans'+topic).html('');
        }
    });
  }else{
    e.preventDefault();
  }
});

$('.editbutton').click(function(e){
  var id = e.target.id.split('_')[1];
  var pid = "#ans_"+id;
  var oldtext = $(pid).html();
  var formedit = '<textarea name="ans" class="form-control" rows="4" id="ed_textarea_ans_'+id+'">'+oldtext+'</textarea>';
  formedit += '<div class="text-right" style="margin:3px;"><button type="button" class="btn btn-outline-danger btn-sm canc_ed" id="canc_ed_'+id+'" onclick="cancel_edit('+id+')">Cancel</button>';
  formedit += '<button type="button" class="btn btn-outline-success btn-sm save_ed" id="save_ed_'+id+'" onclick="save_edited('+id+')">Save</button></div>';
  $(pid).html(formedit);
  $('#ed_'+id).hide();
  $('#del_'+id).hide();
});

function cancel_edit(e){
  var id = e;
  var tid = "#ed_textarea_ans_"+id;
  var pid = "#ans_"+id;
  var oldtext = $(tid).html();
  $(pid).html(oldtext);
  $('#ed_'+id).show();
  $('#del_'+id).show();
};

function save_edited(e){
  var id = e;
  var tid = "#ed_textarea_ans_"+id;
  var pid = "#ans_"+id;
  var newtext = $(tid).val();
  var secur = $("input[name = 'csrfmiddlewaretoken']").val();
  $.ajax({
      url:'/sp1/'+id+'/upd_answer/',
      type: "POST",
      data: {ans: newtext, csrfmiddlewaretoken: secur},
      success:function(response){
        $(pid).html(newtext);
        $('#ed_'+id).show();
        $('#del_'+id).show();
      }
  });
};
