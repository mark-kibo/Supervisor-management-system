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
                columns: [0, 1, 2, 3, 4]
            }
        },
        {
            //excel
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
        },
        {
            //print
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Print',
            //font size on export
            customize: function ( win ){
                $(win.document.body).css('font-size', '10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size', 'inherit');
            }
           
        },
        {
            //pdf
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            //choose columns to export to pdf
            exportOptions: {
                columns: [0, 1, 2, 3, 4]
            },
            //center table
            tableHeader: {
                alignment : 'center'
            },
            //font size and optimization
            customize: function (doc) {
                doc.styles.tableHeader.alignment = 'center'; //header position
                doc.styles.tableBodyOdd.alignment = 'center'; //Body position 1
                doc.styles.tableBodyEven.alignment = 'center'; //Body position 1
                doc.styles.tableHeader.fontSize = 10; //header font-size
                doc.defaultStyle.fontSize = 9; //header position
                // to get 100 % width of table
                doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            }
        }
    ]
} );