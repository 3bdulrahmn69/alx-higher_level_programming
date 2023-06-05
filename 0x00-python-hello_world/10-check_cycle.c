#include "lists.h"

/**
 * check_cycle - C function that checks if a singly linked list has a cycle
 * @list: pointer to the beginning of the node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *now;
	listint_t *checker;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	now = list;
	checker = now->next;

	while (now != NULL && checker->next != NULL && checker->next->next != NULL)
	{
		if (now == checker)
		{
			return (1);
		}
		now = now->next;
		checker = checker->next->next;
	}
	return (0);
}
