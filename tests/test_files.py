import pytest


# Dummy imports or tests for student tasks
def test_organizer_raises_not_implemented():
    """Test that organizer function raises NotImplementedError initially."""
    from automations.files.organizer import organize_directory

    with pytest.raises(NotImplementedError):
        organize_directory("/tmp/some_dir")


def test_backup_raises_not_implemented():
    """Test that backup function raises NotImplementedError initially."""
    from automations.files.backup import backup_folder

    with pytest.raises(NotImplementedError):
        backup_folder("/tmp/src", "/tmp/dest")
