#include <stdio.h>
#include "lists.h"
/**
  * check_cycle - Check for a loop in a linkedlist
  * @list: The head of the list.
  *
  * Return: 1 for cycle, 0 for no cycle.
  */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	/* Return 0 for empty list */
	if (!list)
		return (0);

	/* Separate fast and slow node */
	fast = list->next;
	slow = list;

	/* Keep navigating untill the end of the loop */
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Return NULL if they dont meet */
	return (0);
}
