from django.db import models


class Organism(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name


class ConcentrationMethod(models.Model):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = 'Concentration Method'
        verbose_name_plural = 'Concentration Methods'

    def __str__(self):
        return self.name


class ReadLength(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = 'Read Length'
        verbose_name_plural = 'Read Lengths'

    def __str__(self):
        return self.name


class IndexType(models.Model):
    name = models.CharField('Name', max_length=150)
    is_index_i7 = models.BooleanField('Is Index I7?', default=False)
    is_index_i5 = models.BooleanField('Is Index I5?', default=False)

    class Meta:
        verbose_name = 'Index Type'
        verbose_name_plural = 'Index Types'

    def __str__(self):
        return self.name


class GenericIndex(models.Model):
    index_id = models.CharField('Index ID', max_length=50, unique=True)
    index = models.CharField('Index', max_length=8)
    index_type = models.ForeignKey(IndexType, verbose_name='Index Type')

    class Meta:
        abstract = True

    def __str__(self):
        return self.index_id


class IndexI7(GenericIndex):
    class Meta:
        verbose_name = 'Index I7'
        verbose_name_plural = 'Indices I7'


class IndexI5(GenericIndex):
    class Meta:
        verbose_name = 'Index I5'
        verbose_name_plural = 'Indices I5'


class BarcodeSingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(BarcodeSingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class BarcodeCounter(BarcodeSingletonModel):
    counter = models.PositiveSmallIntegerField(default=0)

    def increment(self):
        self.counter += 1

    def __str__(self):
        return str(self.counter)


class GenericLibrarySample(models.Model):
    name = models.CharField(
        'Name',
        max_length=200,
        unique=True,
    )

    date = models.DateTimeField('Date', auto_now_add=True)

    status = models.SmallIntegerField(default=0)

    organism = models.ForeignKey(
        Organism,
        related_name='organism',
        verbose_name='Organism'
    )

    concentration = models.FloatField('Concentration')

    concentration_determined_by = models.ForeignKey(
        ConcentrationMethod,
        related_name='concentration_determined_by',
        verbose_name='Concentration Determined by',
    )

    dna_dissolved_in = models.CharField('DNA Dissolved in', max_length=255)

    sample_volume = models.PositiveIntegerField('Sample Volume')

    equal_representation_nucleotides = models.BooleanField(
        'Equal Representation of Nucleotides',
        default=False,
    )

    read_length = models.ForeignKey(
        ReadLength,
        related_name='related_name',
        verbose_name='Read Length',
    )

    sequencing_depth = models.PositiveIntegerField('Sequencing Depth')

    comments = models.TextField('Comments', null=True, blank=True)

    is_in_request = models.BooleanField('Is in request?', default=False)

    is_pooled = models.BooleanField('Is pooled?', default=False)

    # barcode = models.CharField(
    #     'Barcode',
    #     max_length=9,
    #     null=True,
    #     blank=True,
    # )

    barcode = models.CharField('Barcode', max_length=9)

    index_type = models.ForeignKey(
        IndexType,
        related_name='index_type',
        verbose_name='Index Type',
        null=True,
        blank=True,
    )

    index_i7 = models.CharField(
        'Index I7',
        max_length=8,
        null=True,
        blank=True,
    )

    index_i5 = models.CharField(
        'Index I5',
        max_length=8,
        null=True,
        blank=True,
    )

    # Quality Control
    dilution_factor = models.PositiveIntegerField(
        'Dilution Factor (facility)',
        null=True,
        blank=True,
    )

    concentration_facility = models.FloatField(
        'Concentration (facility)',
        null=True,
        blank=True,
    )

    concentration_determined_by_facility = models.ForeignKey(
        ConcentrationMethod,
        related_name='concentration_determined_by_facility',
        verbose_name='Concentration Determined by (facility)',
        null=True,
        blank=True,
    )

    date_facility = models.DateTimeField(
        'Date (facility)',
        null=True,
        blank=True,
    )

    sample_volume_facility = models.PositiveIntegerField(
        'Sample Volume (facility)',
        null=True,
        blank=True,
    )

    amount_facility = models.FloatField('Amount', null=True, blank=True)

    size_distribution_facility = models.CharField(
        'Size Distribution (facility)',
        max_length=200,
        null=True,
        blank=True,
    )

    comments_facility = models.TextField(
        'Comments (facility)',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name