#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: The head of the linked list
 *
 * Return: The new head of the reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *mid = NULL;
    listint_t *second_half = NULL;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (palindrome);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        mid = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    second_half = reverse_list(slow);

    while (second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            palindrome = 0;
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    reverse_list(mid);
    return palindrome;
}

/**
 * listint_len - Counts the number of elements in a linked list
 * @h: The linked list to count
 *
 * Return: Number of elements in the linked list
 */
size_t listint_len(const listint_t *h)
{
    size_t length = 0;

    while (h != NULL)
    {
        length++;
        h = h->next;
    }

    return (length);
}

