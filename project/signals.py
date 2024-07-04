import csv
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from project.models import Block, MainChart, ChildChart


@receiver(post_save, sender=Block, dispatch_uid="generate_charts")
def generate_chrats(sender, instance, created, **kwargs):
    """Generate Charts"""
    if created:
        with open(instance.main_csv_data.path, "r", encoding="utf-8") as main_csv_file:
            reader = csv.DictReader(main_csv_file)
            for row in reader:
                main = MainChart.objects.create(
                    index=row["index"],
                    label=row["label"],
                    percent=int(row["percent"]),
                    color=row["color"],
                    block=instance,
                )
                main.save()

                with open(instance.child_csv_file.path, "r", encoding="utf-8") as child_csv_file:
                    child_reader = csv.DictReader(child_csv_file)
                    for row in child_reader:
                        main_id = int(row["main_id"])

                        if main_id == main.index:
                            child = ChildChart.objects.create(
                                index=row["index"],
                                label=row["label"],
                                percent=int(row["percent"]),
                                color=row["color"],
                                main=main,
                            )
                            child.save()
