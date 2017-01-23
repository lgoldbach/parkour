Ext.define('MainHub.view.librarypreparation.LibraryPreparation', {
    extend: 'Ext.container.Container',
    xtype: 'library-preparation',

    requires: [
        'MainHub.view.librarypreparation.LibraryPreparationController',
        'MainHub.view.librarypreparation.BenchtopProtocolWindow',
        'Ext.ux.FiddleCheckColumn'
    ],

    controller: 'library-preparation',

    anchor: '100% -1',
    layout: 'fit',

    items: [{
        xtype: 'grid',
        id: 'libraryPreparationTable',
        itemId: 'libraryPreparationTable',
        height: Ext.Element.getViewportHeight() - 64,
        header: {
            title: 'Library Preparation'
        },
        padding: 15,
        viewConfig: {
            markDirty: false
        },
        plugins: [{
                ptype: 'rowediting',
                clicksToEdit: 2
            },
            {
                ptype: 'bufferedrenderer',
                trailingBufferZone: 100,
                leadingBufferZone: 100
            }
        ],
        features: [{
            ftype: 'grouping',
            groupHeaderTpl: '<strong>Protocol: {name}</strong>'
        }],
        store: 'libraryPreparationStore',

        columns: [{
                xtype: 'fiddlecheckcolumn',
                text: 'Active',
                dataIndex: 'active',
                width: 40
            },
            {
                text: 'Sample',
                dataIndex: 'name',
                width: 200
            },
            {
                text: 'Barcode',
                dataIndex: 'barcode',
                width: 90
            },
            {
                text: 'Concentration Sample (ng/µl)',
                dataIndex: 'concentrationSample'
            },
            {
                text: 'Protocol',
                dataIndex: 'libraryProtocolName'
            },
            {
                text: 'Starting Amount (ng)',
                dataIndex: 'startingAmount',
                editor: {
                    xtype: 'numberfield',
                    decimalPrecision: 1,
                    minValue: 1
                }
            },
            {
                text: 'Starting Volume (ng)',
                dataIndex: 'startingVolume',
                editor: {
                    xtype: 'numberfield',
                    decimalPrecision: 1,
                    minValue: 1
                }
            },
            {
                text: 'Spike-in Description',
                dataIndex: 'spikeInDescription',
                editor: {
                    xtype: 'textarea'
                }
            },
            {
                text: 'Spike-in Volume (µl)',
                dataIndex: 'spikeInVolume',
                editor: {
                    xtype: 'numberfield',
                    decimalPrecision: 1,
                    minValue: 1
                }
            },
            {
                text: 'µl Sample',
                dataIndex: 'ulSample',
                editor: {
                    xtype: 'numberfield',
                    decimalPrecision: 1,
                    minValue: 0.1
                }
            },
            {
                text: 'µl Buffer',
                dataIndex: 'ulBuffer',
                editor: {
                    xtype: 'numberfield',
                    decimalPrecision: 1,
                    minValue: 0.1
                }
            },
            {
                text: 'Index I7 ID',
                dataIndex: 'indexI7Id'
            },
            {
                text: 'Index I5 ID',
                dataIndex: 'indexI5Id'
            },
            {
                text: 'PCR Cycles',
                dataIndex: 'pcrCycles',
                editor: {
                    xtype: 'numberfield',
                    allowDecimals: false,
                    minValue: 1
                }
            },
            {
                text: 'Concentration Library (ng/µl)',
                dataIndex: 'concentrationLibrary',
                editor: {
                    xtype: 'numberfield',
                    minValue: 1
                }
            },
            {
                text: 'Mean Fragment Size (bp)',
                dataIndex: 'meanFragmentSize',
                editor: {
                    xtype: 'numberfield',
                    allowDecimals: false,
                    minValue: 1
                }
            },
            {
                text: 'nM',
                dataIndex: 'nM',
                editor: {
                    xtype: 'numberfield',
                    minValue: 1
                }
            },
            {
                text: 'File',
                dataIndex: 'file',
                width: 45,
                renderer: function(value) {
                    return (value !== '') ? '<a class="library-preparation-download" href="' +
                        value + '">' + '<i class="fa fa-download" aria-hidden="true"></i></a>' : '';
                }
            },
            {
                text: 'QC Result',
                dataIndex: 'qcResult',
                editor: {
                    xtype: 'combobox',
                    queryMode: 'local',
                    displayField: 'name',
                    valueField: 'id',
                    store: Ext.create('Ext.data.Store', {
                        fields: [{
                                name: 'id',
                                type: 'int'
                            },
                            {
                                name: 'name',
                                type: 'string'
                            }
                        ],
                        data: [{
                                id: 1,
                                name: 'passed'
                            },
                            {
                                id: 2,
                                name: 'failed'
                            }
                        ]
                    }),
                    forceSelection: true
                }
            }
        ],
        dockedItems: [{
            xtype: 'toolbar',
            dock: 'bottom',
            items: [
                '->',
                {
                    xtype: 'button',
                    id: 'downloadBenchtopProtocolLPBtn',
                    itemId: 'downloadBenchtopProtocolLPBtn',
                    text: 'Download Benchtop Protocol as XLS',
                    disabled: true
                }
            ]
        }]
    }]
});
