Ext.define('MainHub.model.libraries.Library', {
    extend: 'MainHub.model.Base',

    fields: [{
            name: 'status',
            type: 'int'
        },
        {
            name: 'requestName',
            type: 'string'
        },
        {
            name: 'requestId',
            type: 'int'
        },
        {
            name: 'libraryId',
            type: 'int'
        },
        {
            name: 'sampleId',
            type: 'int'
        },
        {
            name: 'name',
            type: 'string'
        },
        {
            name: 'recordType',
            type: 'string'
        },
        {
            name: 'date',
            type: 'string'
        },
        {
            name: 'libraryProtocol',
            type: 'string'
        },
        {
            name: 'libraryProtocolId',
            type: 'int'
        },
        {
            name: 'libraryType',
            type: 'string'
        },
        {
            name: 'libraryTypeId',
            type: 'int'
        },
        {
            name: 'enrichmentCycles',
            type: 'string'
        },
        {
            name: 'amplifiedCycles',
            type: 'string'
        },
        {
            name: 'organism',
            type: 'string'
        },
        {
            name: 'organismId',
            type: 'int'
        },
        {
            name: 'indexType',
            type: 'string'
        },
        {
            name: 'indexTypeId',
            type: 'int'
        },
        {
            name: 'indexReads',
            type: 'string'
        },
        {
            name: 'indexI7',
            type: 'string'
        },
        {
            name: 'indexI5',
            type: 'string'
        },
        {
            name: 'equalRepresentation',
            type: 'string'
        },
        {
            name: 'DNADissolvedIn',
            type: 'string'
        },
        {
            name: 'concentration',
            type: 'string'
        },
        {
            name: 'concentrationMethod',
            type: 'string'
        },
        {
            name: 'concentrationMethodId',
            type: 'int'
        },
        {
            name: 'sampleVolume',
            type: 'string'
        },
        {
            name: 'meanFragmentSize',
            type: 'string'
        },
        {
            name: 'qPCRResult',
            type: 'string'
        },
        {
            name: 'readLength',
            type: 'string'
        },
        {
            name: 'readLengthId',
            type: 'int'
        },
        {
            name: 'sequencingDepth',
            type: 'string'
        },
        {
            name: 'comments',
            type: 'string'
        },
        {
            name: 'barcode',
            type: 'string'
        },

        {
            name: 'nucleicAcidType',
            type: 'string'
        },
        {
            name: 'nucleicAcidTypeId',
            type: 'int'
        },
        {
            name: 'DNaseTreatment',
            type: 'string'
        },
        {
            name: 'rnaQuality',
            type: 'string'
        },
        {
            name: 'rnaSpikeIn',
            type: 'string'
        },
        {
            name: 'samplePreparationProtocol',
            type: 'string'
        },
        {
            name: 'requestedSampleTreatment',
            type: 'string'
        }
    ]
});
