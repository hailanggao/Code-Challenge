<template>
  <v-card>
    <v-card-title>
      Organisation List <v-btn icon @click="dialog = true"><v-icon>mdi-plus</v-icon></v-btn>
    </v-card-title>
    <v-data-table :headers="headers" :items="organisations">
      <template v-slot:item.active="{ item }">
        <v-btn icon @click="deleteOrganisation(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
        <v-btn
          icon
          @click="
            organisation_id = item.id
            dialog = true
          "
          ><v-icon>mdi-pen</v-icon>
        </v-btn>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog">
      <organisation-form
        @save="
          dialog = false
          getOrganisations()
        "
      />
    </v-dialog>
  </v-card>
</template>

<script>
import OrganisationForm from '../components/OrganisationForm.vue'
export default {
  components: { OrganisationForm },

  data() {
    return {
      dialog: false,
      organisations: [],
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Address', value: 'address' },
        { text: 'Post Code', value: 'postcode' },
        { text: 'Contact Name', value: 'contact_name' },
        { text: 'Contact Phone', value: 'contact_phone' },
        { text: 'Contact Email', value: 'contact_email' },
        { text: 'Departments', value: 'departments' },
      ],
    }
  },

  created() {
    this.getOrganisations()
  },

  methods: {
    async getOrganisations() {
      const orgs = await this.$axios.$get('/organisation/organisations')
      const counts = orgs.reduce((total, org) => total + org.departments, 0)
      this.organisations = [...orgs, { name: 'Totals', departments: counts }]
    },

    async deleteOrganisation(id) {
      await this.$axios.$delete('/organisation/organisation', { params: { id } })
      this.getOrganisations()
    },
  },
}
</script>

<style></style>
