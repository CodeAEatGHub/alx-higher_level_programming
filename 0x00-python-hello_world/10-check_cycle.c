#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for loops in a list
 * @h: pointer to head of list
 * Return: o if there is no loop
 */
int check_cycle(listint_t *list)
{
    const listint_t *current;

    current = list;
    while (current != NULL)
    {
        if (current < current->next)
        	return (0);
	else
	{
		current = current->next;
		continue;
	}
    }
    return (1);
}
