$(document).ready(function() {
    // edit item
    $(".edit-btn").on('click', function () {
      var itemId = this.id;
      $("#item" + itemId).hide();
      $("#form" + itemId).show();
      $(".cancel-btn").click(function() {
          $("#form" + itemId).hide();
          $("#item" + itemId).show();
      });
    });

  })

  // echarts
