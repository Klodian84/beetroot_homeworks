class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  # Private workers list

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        """Adds a Worker instance to the boss's workers list."""
        if isinstance(worker, Worker):
            if worker not in self._workers:
                self._workers.append(worker)
                worker.boss = self
        else:
            raise TypeError("Only instances of Worker can be added as workers.")

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        """Sets a new boss for the worker and validates it's an instance of Boss."""
        if isinstance(boss, Boss):
            if self._boss != boss:
                # Remove worker from the old boss's workers list if reassigning
                if self._boss:
                    self._boss.workers.remove(self)
                self._boss = boss
                # Add this worker to the new boss's workers list
                if self not in boss.workers:
                    boss.add_worker(self)
        else:
            raise TypeError("Boss must be an instance of Boss.")


# Boss instance
boss1 = Boss(1, "John", "Tech Corp")

# Worker instance with a valid boss
worker1 = Worker(101, "Alice", "Tech Corp", boss1)

# New boss
boss2 = Boss(2, "Jane", "Innovate Inc")

# Reassign the worker to a new boss
worker1.boss = boss2

# Verify the workers list of both bosses
print(f"Boss {boss1.name} now has workers: {[worker.name for worker in boss1.workers]}")
print(f"Boss {boss2.name} has workers: {[worker.name for worker in boss2.workers]}")

