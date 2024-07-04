import csv
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from project.models import Block, MainChart, ChildChart, ChartType


@receiver(post_save, sender=Block, dispatch_uid="generate_charts")
def generate_chrats(sender, instance, created, **kwargs):
    """Generate Charts"""
    if instance.type_csv_file and instance.main_csv_file and instance.child_csv_file:
        with open(instance.type_csv_file.path, "r", encoding="utf-8") as type_csv_file:
            reader = csv.DictReader(type_csv_file)
            for row in reader:
                type = ChartType.objects.create(
                    index=row["index"],
                    label=row["label"],
                    block=instance
                )
                type.save()
                with open(instance.main_csv_file.path, "r", encoding="utf-8") as main_csv_file:
                    reader = csv.DictReader(main_csv_file)
                    for row in reader:
                        type_id = 0
                        try:
                            type_id = int(row["type_id"])
                        except:
                            pass
                        
                        if type_id == int(type.index):
                            main = MainChart.objects.create(
                                index=row["index"],
                                label=row["label"],
                                percent=int(row["percent"]),
                                color=row["color"],
                                type=type,
                            )
                            main.save()

                            with open(instance.child_csv_file.path, "r", encoding="utf-8") as child_csv_file:
                                child_reader = csv.DictReader(child_csv_file)
                                for row in child_reader:
                                    main_id = 0
                                    try:
                                        main_id = int(row["main_id"])
                                    except:
                                        pass

                                    if main_id == int(main.index):
                                        child = ChildChart.objects.create(
                                            index=row["index"],
                                            label=row["label"],
                                            percent=int(row["percent"]),
                                            color=row["color"],
                                            main=main,
                                        )
                                        child.save()
