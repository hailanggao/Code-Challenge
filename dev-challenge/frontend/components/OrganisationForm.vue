<template>
  <v-card>
    <v-card-title> Add Organisation </v-card-title>
    <v-card-text>
      <v-text-field v-model="organisation.name" label="Name" />
      <v-text-field v-model="organisation.address" label="Address" />
      <v-text-field v-model="organisation.postcode" label="Post-Code" />
      <v-text-field v-model="organisation.contact_name" label="Contact-Name" />
      <v-text-field v-model="organisation.contact_phone" label="Contact-Phone" />
      <v-text-field v-model="organisation.contact_email" label="Contact-Email" />
      <v-text-field v-model="organisation.departments" label="Departments" />
    </v-card-text>
    <v-card-actions>
      <v-btn v-if="!update" :disabled="lock" color="primary" @click="addOrganisation()">Save</v-btn>
      <v-btn v-else :disabled="lock" color="primary" @click="updateOrganisation()">Update</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['organisation_id'],
  data() {
    return {
      organisation: {},
      lock: false,
      update: false,
    }
  },
  watch: {
    organisation_id() {
      if (this.organisation_id) {
        this.update = true
        this.getOrganisation(this.organisation_id)
      } else {
        this.update = false
        this.organisation = {}
      }
    },
  },
  crated() {
    if (this.organisation_id) {
      this.update = true
      this.organisation(this.organisation_id)
    } else {
      this.update = false
      this.organisation = {}
    }
  },
  methods: {
    async addOrganisation() {
      this.lock = true
      await this.$axios.$post('/organisation/organisation', this.organisation)
      this.lock = false
      this.organisation = {}
      this.$emit('save')
    },
    async getOrganisation(id) {
      const org = await this.$axios.$get(`/organisation/organisation?id=${id}`)
      this.organisation = org
    },
    async updateOrganisation(){
      this.lock = true
      await this.$axios.$put(`/organisation/organisation?id=$(this.organisation_id)`, this.organisation)
      this.lock = false
      this.organisation = {}
      this.$emit('save')
    },
  },
}
</script>

<style></style>
