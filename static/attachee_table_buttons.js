$('#dataTable').DataTable( {
    dom: 'lBfrtip',
    buttons: [
        {
            extend: 'copy',
            text: '<i class="fas fa-clone"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Copy',
            //choose columns to copy
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
            }
        },
        {
            //excel
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
            }
        },
        {
            //print
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Print',
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5, 6, 7, 8]
            },
            //font size on export
            customize: function ( win ){
                $(win.document.body).css('font-size', '10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size', 'inherit');
            }
           
        },
    
    ]
} );