from django.db import models
from django.utils.translation import gettext_lazy as _


class Midi(models.Model):
    DIFFICULTY_VERY_EASY = 0
    DIFFICULTY_EASY = 1
    DIFFICULTY_NORMAL = 2
    DIFFICULTY_HARD = 3
    DIFFICULTY_VERY_HARD = 4
    DIFFICULTIES = (
        (DIFFICULTY_VERY_EASY, _('Very easy')),
        (DIFFICULTY_EASY, _('Easy')),
        (DIFFICULTY_NORMAL, _('Normal')),
        (DIFFICULTY_HARD, _('Hard')),
        (DIFFICULTY_VERY_HARD, _('Very hard')),
    )

    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True)
    file = models.FileField(_('File'), upload_to='files/midi')
    image = models.ImageField(_('Image'), upload_to='images/midi')
    difficulty = models.PositiveSmallIntegerField(_('Difficulty'), choices=DIFFICULTIES, default=DIFFICULTY_NORMAL)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('MIDI file')
        verbose_name_plural = _('MIDI files')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Midi(pk={self.pk}, title={self.title})'
